import argparse
import json
import re

from tqdm import tqdm

parser = argparse.ArgumentParser(description='Preprocess HotpotQA')
parser.add_argument('-j', '--json', help='HotpotQA json file to preprocess')
parser.add_argument('-t', '--txt', help='txt file to store the labelled result')
parser.add_argument('-l', '--label', help='label for the questions in the file')
parser.add_argument('-w', '--wh', help="Pick only questions that begin with 'wh' and end with '?'")

args = vars(parser.parse_args())

if __name__ == '__main__':
    json_filepath = args['json']
    txt_filepath = args['txt']
    label = args['label']
    wh = True if args['wh'] == 'true' else False

    with open(json_filepath) as f:
        json_file = json.load(f)

    txt_file = open(txt_filepath, 'a')

    wh_pattern = r"^wh.*\?$"
    
    all_questions = []

    for _, q in tqdm(json_file.items(), desc=f'Labelling questions from {json_filepath}: '):
        if wh:
            if re.match(wh_pattern, q.lower()):
                if args['label'] is not None:
                    text = f'{label} {q}'
                else:
                    text = q
                all_questions.append(text)
        else:
            if args['label'] is not None:
                text = f'{label} {q}'
            else:
                text = q
            all_questions.append(text)

    questions = '\n'.join(all_questions)
    
    txt_file.write('\n')
    txt_file.write(questions)

    f.close()
    txt_file.close()