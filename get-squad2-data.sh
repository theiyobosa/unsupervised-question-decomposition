#!/bin/bash

# Create the folder to store the data
squad2_raw_dir=squad2/raw
squad2_q_only_dir=squad2/question_only

if [ ! -d $squad2_raw_dir ]; then
    mkdir -p $squad2_raw_dir
    mkdir -p $squad2_q_only_dir
fi

squad2_filenames=(train-v2.0.json
                  dev-v2.0.json)

for fname in "${squad2_filenames[@]}"
do
    if [ ! -f $squad2_raw_dir/$fname ]; then
        wget -P $squad2_raw_dir https://rajpurkar.github.io/SQuAD-explorer/dataset/$fname
    fi
done

# Process questions only
for file in $squad2_raw_dir/*
do
    python preprocessing/squad2/question_only.py -f $file -d $squad2_q_only_dir
done

# Create train data
train_data=train_data.txt
dev_data=dev_data.txt

train_json_file=$squad2_q_only_dir/${squad2_filenames[0]}
dev_json_file=$squad2_q_only_dir/${squad2_filenames[1]}

wh=true

python preprocessing/labeller.py -j $train_json_file -t $train_data -l __label__2 --wh $wh
python preprocessing/labeller.py -j $dev_json_file -t $dev_data -l __label__2 --wh $wh