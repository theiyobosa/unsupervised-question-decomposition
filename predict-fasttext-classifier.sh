#!/bin/bash

cd fastText

./fasttext predict ../fasttext_model.bin ../train_data_mfaq.txt > ../train_data_mfaq_predict.txt