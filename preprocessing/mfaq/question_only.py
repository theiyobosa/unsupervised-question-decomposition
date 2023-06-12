import argparse
from ast import literal_eval
import json
from os.path import basename, join

from tqdm import tqdm

parser = argparse.ArgumentParser(description='Preprocess HotpotQA')
parser.add_argument('-f', '--file', help='HotpotQA json file to preprocess')
parser.add_argument('-d', '--dir', help='Directory to store the result')

args = vars(parser.parse_args())

if __name__ == '__main__':
    filepath = args['file']
    dir = args['dir']

    json_file = open(filepath, 'r')

    questions = dict()
    with open(filepath, 'r') as f:
        i = 0
        for line in tqdm(f, desc=f'Extracting questions from {filepath}: '):
            jl = literal_eval(line)
            questions[i] = jl['question']
            i += 1

    fname = basename(filepath)
    new_filepath = join(dir, fname)

    new_file = open(new_filepath, 'w')
    json.dump(questions, new_file)

    json_file.close()
    new_file.close()