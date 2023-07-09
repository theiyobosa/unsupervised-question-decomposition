from argparse import ArgumentParser

from fasttext import load_model
from tqdm import tqdm

from config import *
from create_db import ping_db, confirm_index


parser = ArgumentParser(description='Upload question data to database')
parser.add_argument('-f', '--file', help='The path of the txt file containing \
                                          the questions and their labels')
parser.add_argument('-m', '--model', help='Path to the fastText model')
parser.add_argument('-d', '--dim', help='The dimension of the vectors in the \
                                         database')

args = vars(parser.parse_args())

if __name__ == '__main__':
    file = args['file']
    model_path = args['model']
    dims = int(args['dim'])

    connection = ping_db(ip=IP, port=PORT)

    confirm_index(connection, Q_INDEX, dims)
    confirm_index(connection, S_INDEX, dims)

    with open(file, encoding='utf8') as f:
        data = f.read().split('\n')
        print(len(data))

    model = load_model(model_path)

    label = '__label__'
    s_label = '__label__S '
    q_label = '__label__Q '

    s_count = connection.count(index=S_INDEX)['count']
    q_count = connection.count(index=Q_INDEX)['count']

    print('Uploading:', file)

    print('Initial S count:', s_count)
    print('Initial Q count:', q_count)

    for d in tqdm(data):
        if d.startswith(label):
            lbl = s_label if d.startswith(s_label) else q_label

            question = d.replace(lbl, '')
            vector = model.get_sentence_vector(question).tolist()

            if lbl == s_label:
                connection.index(index=S_INDEX,
                                 body={
                                     'question': question,
                                     'vector': vector,
                                     'id': s_count
                                 })
                
                s_count += 1

            elif lbl == q_label:
                connection.index(index=Q_INDEX,
                                 body={
                                     'question': question,
                                     'vector': vector,
                                     'id': q_count
                                 })
                
                q_count += 1

    print('Final S count:', s_count)
    print('Final Q count:', q_count)
    print('Completed...')