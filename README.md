This repository contains the WikiSem500 dataset described in "Automated Generation of Multilingual Clusters for Word Embedding Evaluation" by Philip Blair, Yuval Merhav, and Joel Barry.

The test groups themselves can be found in `wiki-sem-500.tar.gz` (`wiki-sem-500-tokenized.tar.gz` is pre-tokenized). The structure of the archive is as follows:

```
wiki-sem-500
├── de
│   ├── Q101352.txt
│   ├── Q105000.txt
│   ├── Q1061151.txt
│   ├── Q1065118.txt
│   ...
├── en
│   ├── Q101352.txt
│   ...
├── es
│   ├── Q101352.txt
│   ...
├── ja
│   ├── Q101352.txt
│   ...
├── zh
│   ├── Q101352.txt
│   ...
```

Note that while many classes are available in multiple languages, there are many that are not.

Each file contains a cluster, followed by a sequence of one or more outliers:
```
$ cat en/Q1060829.txt

Madison_Square_Garden
Walt_Disney_Concert_Hall
Olympia
Kodak_Theatre
Carnegie_Hall
Auditorio_de_Tenerife
Royal_Albert_Hall
Palau_de_la_Música_Catalana

CBGB
Buena_Vista_Social_Club
Arena_di_Verona
Barbican_Centre
RMS
HMHS
```


## Running the Evaluation Script
To run the evaluation script, navigate to this directory in a virtualenv
and run `install_dependencies.py` . The embeddings are driven by a partial
fork of [`polyglot`][polyglot].

Once the dependencies are installed, unpack the *tokenized* dataset at a location
of your choice (say, `dataset/`). A word2vec binary embedding can then be evaluated as
follows:

```
(venv2) $ ./evaluate.py -w2v vectors.bin -d dataset/en -b
```

GloVe and Gensim embeddings are also supported. Here is the full help message for
`evaluate.py`:

```
usage: evaluate.py [-h] (-w2v WORD2VEC | -gv GLOVE | -gs GENSIM) -d DATASET
                   [-b] [-p] [-goog] [-ci CASE_INSENSITIVE]

Scoring script for outlier detection

optional arguments:
  -h, --help            show this help message and exit
  -w2v WORD2VEC, --word2vec WORD2VEC
                        Specify word2vec embedding file
  -gv GLOVE, --glove GLOVE
                        Specify GloVe embedding file
  -gs GENSIM, --gensim GENSIM
                        Specify Gensim embedding file
  -d DATASET, --dataset DATASET
                        Path to outlier dataset
  -b, --binary          Indicates that the embedding file is binary (ignored
                        for GloVe files)
  -p, --phrases         Indicates that the embedding file supports phrases
  -goog, --google-news  Indicates that the embeddings have been normalized in
                        the same fashion as the Google News word2vec
                        embeddings
  -ci CASE_INSENSITIVE, --case-insensitive CASE_INSENSITIVE
                        Indicates whether the embeddings are all lowercased
```


[polyglot]: https://github.com/aboSamoor/polyglot/
