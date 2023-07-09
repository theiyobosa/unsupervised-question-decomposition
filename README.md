# Unsupervised Question Decomposition

This project is about finding ways to break down questions, before they are answered, using unsupervised techniques. The aim is to improve context in LLM solutions.

**Example**

Question: What school did James Maxwell's lawyer graduate from?

Breakdown (Decomposition):
- Who is James Maxwell?
- Who is his lawyer?
- What school did he graduate from?

# Setup

Environment:

- Linux
- [Python 3.10.9](https://www.python.org/downloads/release/python-3109/)
- [Elasticsearch 7.9.1](https://www.elastic.co/downloads/past-releases/elasticsearch-7-9-1)

## Database

Untar the Elasticsearch v7.9.1 that was downloaded:

```bash
tar -xvzf elasticsearch_file.tar.gz
```

Boot it up:

```bash
tar -xvzf elasticseach-7.9.1/bin/elasticsearch
```

## Dataset

Download and preprocess the HotpotQA, SQuAD, and MFAQ datasets:

```bash
bash get-dataset.sh
```

Get the fastText package:

```bash
bash get-fasttext.sh
```

Train the classifier on HotpotQA and SQuAD datasets:

```bash
bash train-fasttext-classifier.sh
```

Make predictions on the MFAQ dataset from the trained classifier:

```bash
bash predict-fasttext-classifier.sh
```

Upload the data to Elasticsearch with:

```bash
bash upload-to-elasticsearch.sh
```