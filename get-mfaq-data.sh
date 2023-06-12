#!/bin/bash

# Get mfaq_light data from Hugging Face

# Create the folder to store the data
mfaq_raw_dir=mfaq/raw
mfaq_q_only_dir=mfaq/question_only

if [ ! -d $mfaq_raw_dir ]; then
    mkdir -p $mfaq_raw_dir
    mkdir -p $mfaq_q_only_dir
fi

mfaq_filenames=(train.json valid.json)

for fname in "${mfaq_filenames[@]}"
do
     if [ ! -f $mfaq_raw_dir/$fname ]; then
          wget -O $mfaq_raw_dir/$fname https://huggingface.co/datasets/maximedb/mfaq_light/resolve/main/data/${fname%.*}/data.en.json
     fi
done

# Process questions only
for file in $mfaq_raw_dir/*
do
    python preprocessing/mfaq/question_only.py -f $file -d $mfaq_q_only_dir
done

# # Create train data
train_data=train_data_mfaq.txt
dev_data=dev_data_mfaq.txt

train_json_file=$mfaq_q_only_dir/${mfaq_filenames[0]}
dev_json_file=$mfaq_q_only_dir/${mfaq_filenames[1]}

wh=true

python preprocessing/labeller.py -j $train_json_file -t $train_data --wh $wh
python preprocessing/labeller.py -j $dev_json_file -t $dev_data --wh $wh