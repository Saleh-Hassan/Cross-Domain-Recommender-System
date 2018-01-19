<h1 align="center">
  <br>
  Cross-Domain-Recommender-System
  <br>
</h1>

![Screenshot](/web_app_image.png?raw=true)

## Key Features

* A web interface for Single-Domain and Cross-Domain Recommender System
* Uses data collected from Facebook about users personal preferences in two domains: movies and books
* Works with RDF dataset generated from Facebook data and contains incoming and outgoing Dbpedia edges for items
* Computes RDF2Vec and Doc2Vec Embeddings for DBpedia graph entities to compute similarities
* To compute RDF2Vec Embeddings:
  - Converts RDF graphs into sequences of entities and relations using Graph Walks
  - Train a neural language model where each entity and relation is represented as N-dimensional numerical vector
* To compute Doc2Vec Embeddings:
  - Along with word vectors, it also trains a paragraph vector which contains numerical representation of DBpedia item abstract
* Computes dot product similarity between latent representation of graph entities and sort items based on similarity scores

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
