<h1 align="center">
  <br>
  Cross-Domain-Recommender-System
  <br>
</h1>

![Screenshot](/web_app_image.png?raw=true)

## Overview

* A web interface for Single-Domain and Cross-Domain Recommender System
* Based on techniques described in [Word2Vec](https://arxiv.org/pdf/1310.4546.pdf), [Doc2Vec](https://cs.stanford.edu/~quocle/paragraph_vector.pdf) and [RDF2Vec](https://ub-madoc.bib.uni-mannheim.de/41307/1/Ristoski_RDF2Vec.pdf)
* Uses dataset collected from Facebook about users' personal preferences in two domains: movies and books
* An RDF dataset is generated from Facebook dataset which contains incoming and outgoing Dbpedia edges for items in FB dataset

## Working

* First it computes RDF2Vec and Doc2Vec Embeddings for DBpedia graph entities to compute similarities between items
* To compute RDF2Vec Embeddings:
  - It converts RDF graphs into sequences of entities and relations using Graph Walks
  - It then trains a neural language model where each entity and relation is represented as N-dimensional numerical vector
* To compute Doc2Vec Embeddings:
  - Along with word vectors, it also trains a paragraph vector which contains numerical representation of item's abstract in DBpedia
* Finally, it computes dot product similarity between latent representation of graph entities and sort items based on similarity scores
* For simplicity, we have already computed Embedding files for Doc2Vec and RDF2Vec and shipping it with the code.

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com), [Python](https://www.python.org/downloads/) and [Pip](https://pypi.python.org/pypi/pip) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/Saleh-Hassan/Cross-Domain-Recommender-System.git

# Go into the repository
$ cd Cross-Domain-Recommender-System

# Create python virtual environment
$ pip install virtualenv
$ virtualenv Cross-Domain-Recommender-System

# Activate virtual environment
$ source Cross-Domain-Recommender-System/bin/activate

# Insall numpy
$ pip install numpy

# Run the app
$ python index.py
```
