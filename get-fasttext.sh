#!/bin/bash

# Install fastText
if [ ! -d fastText ]; then
    echo "Cloning fastText repository"

    git clone https://github.com/facebookresearch/fastText.git

    echo "Installing fastText"
    cd fastText
    make
    cd ..

    echo "fastText installed"
fi