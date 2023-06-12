#!/bin/bash

# Create file to store labelled data for training
> train_data.txt
> dev_data.txt

bash get-hotpotqa-data.sh
bash get-squad2-data.sh
bash get-mfaq-data.sh