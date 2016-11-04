This repository contains the WikiSem500 dataset described in "Automated Generation of Multilingual Clusters for Word Embedding Evaluation" by Philip Blair, Yuval Merhav, and Joel Barry.

The test groups themselves can be found in `wiki-sem-500.tar.gz`. The structure of the archive is as follows:

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

