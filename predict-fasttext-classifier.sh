#!/bin/bash

cd fastText

questions=../train_data_mfaq.txt
labels=../train_data_mfaq_predict.txt

./fasttext predict ../fasttext_model.bin $questions > $labels

python ../preprocessing/merge_label_question.py -q $questions -l $labels

echo "File stored at ${labels}"