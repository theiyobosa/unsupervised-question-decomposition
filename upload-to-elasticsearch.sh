#!/bin/bash

labelled_data=(../train_data.txt ../train_data_mfaq_predict.txt)
model=../fasttext_model.bin
dim=256

cd database

for data in "${labelled_data[@]}"
do
    python upload.py -f $data -m $model -d $dim
done