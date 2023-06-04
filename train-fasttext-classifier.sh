#!/bin/bash

./fasttext supervised -input train_data.txt \
                      -output fasttext_model \
                      -label __label__ \
                      -lr 0.01 \
                      -dim 256 \
                      -ws 5 \
                      -epoch 10 \
                      