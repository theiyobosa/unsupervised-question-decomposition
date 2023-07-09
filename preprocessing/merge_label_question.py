import argparse

from tqdm import tqdm

parser = argparse.ArgumentParser(description='Preprocess HotpotQA')
parser.add_argument('-q', '--question', help='txt file that contains questions')
parser.add_argument('-l', '--label', help='txt file that contains labels for the questions')

args = vars(parser.parse_args())

if __name__ == '__main__':
    question_file = args['question']
    label_file = args['label']

    questions = open(question_file).read().split('\n')
    labels = open(label_file).read().split('\n')

    questions = [i for i in questions if i != '\n' and len(i) != 0]
    labels = [i for i in labels if i != '\n' and len(i) != 0]

    print(len(questions), len(labels))
    print(len(questions[0]))

    label_questions = []

    for i in tqdm(range(len(questions)), desc=f'Joining questions and lables in {question_file} and {label_file}: '):
        q = questions[i]
        l = labels[i]

        if l[-1] == '\n':
            l = l[:-1]

        if q[-1] == '\n':
            q = q[:-1]

        lq = f'{l} {q}'
        label_questions.append(lq)           

    label_questions = '\n'.join(label_questions)
    label_questions = label_questions + '\n'

    final_file = open(label_file, 'w')
    final_file.write(label_questions)

    final_file.close()