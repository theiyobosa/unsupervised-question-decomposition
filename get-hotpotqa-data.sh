#!/bin/bash

# Create the folder to store the data
hotpotqa_raw_dir=hotpotqa/raw
hotpotqa_q_only_dir=hotpotqa/question_only

if [ ! -d $hotpotqa_raw_dir ]; then
    mkdir -p $hotpotqa_raw_dir
    mkdir -p $hotpotqa_q_only_dir
fi

hotpotqa_filenames=(hotpot_train_v1.1.json
                    hotpot_dev_distractor_v1.json
                    hotpot_dev_fullwiki_v1.json
                    hotpot_test_fullwiki_v1.json)

for fname in "${hotpotqa_filenames[@]}"
do
    if [ ! -f $hotpotqa_raw_dir/$fname ]; then
        wget -P $hotpotqa_raw_dir http://curtis.ml.cmu.edu/datasets/hotpot/$fname
    fi
done

# Process questions only
for file in $hotpotqa_raw_dir/*
do
    python preprocessing/hotpotqa/question_only.py -f $file -d $hotpotqa_q_only_dir
done

# Create train data
train_data=train_data.txt
dev_data=dev_data.txt

train_json_file=$hotpotqa_q_only_dir/${hotpotqa_filenames[0]}
dev_json_file=$hotpotqa_q_only_dir/${hotpotqa_filenames[2]}

wh=true

python preprocessing/labeller.py -j $train_json_file -t $train_data -l __label__Q --wh $wh
python preprocessing/labeller.py -j $dev_json_file -t $dev_data -l __label__Q --wh $wh