#!/bin/bash

cd fastText

echo "Training stage"

# Train a fasttext classifier
./fasttext supervised -input ../train_data.txt \
                    -output ../fasttext_model \
                    -label __label__ \
                    -dim 256 \
                    # -ws 5 \
                    # -epoch 10 \
                    # -loss ns \
                    # -lr 0.01 \
                    # -saveOutput 1

echo "Testing state"

# Test on the test set
./fasttext test ../fasttext_model.bin ../dev_data.txt