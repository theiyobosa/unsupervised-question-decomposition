import argparse
import json
from os.path import basename, join

from tqdm import tqdm

parser = argparse.ArgumentParser(description='Preprocess SQuAD 2')
parser.add_argument('-f', '--file', help='SQuAD 2 json file to preprocess')
parser.add_argument('-d', '--dir', help='Directory to store the result')

args = vars(parser.parse_args())

if __name__ == '__main__':
    filepath = args['file']
    dir = args['dir']

    json_file = open(filepath, 'r')
    data = json.load(json_file)
    data = data['data']
    
    questions = dict()
    index = 0
    for i in range(len(data)):
        data_i = data[i]['paragraphs']
        for j in range(len(data_i)):
            data_j = data_i[j]['qas']
            for k in range(len(data_j)):
                data_k = data_j[k]
                questions[index] = data_k['question']
                index += 1
                

    fname = basename(filepath)
    new_filepath = join(dir, fname)

    new_file = open(new_filepath, 'w')
    json.dump(questions, new_file)

    json_file.close()
    new_file.close()