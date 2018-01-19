<h1 align="center">
  <br>
  Cross-Domain-Recommender-System
  <br>
</h1>
----
A web interface for Single-Domain and Cross-Domain Recommender System. We will use data collected from Facebook about personal interests in two domains: movies and books. An RDF dataset was generated from it that contains incoming and outgoing Dbpedia edges for items and resources connected by means of up to three predicates. To compute recommendations, we first compute RDF2Vec and Doc2Vec Embeddings. RDF2Vec is an adaptation of Word2Vec to RDF graphs in which we compute latent representation of graph entities based on graph context. To compute RDF2Vec embeddings, we first convert RDF graphs into sequences of entities and relations using Graph Walks. Then, we train a neural language model where each entity and relation is represented as N-dimensional numerical vector. After computing embeddings, we compute dot product similarity between 

## Key Features

* LivePreview - Make changes, See changes
  - Instantly see what your Markdown documents look like in HTML as you create them.
* Sync Scrolling
  - While you type, LivePreview will automatically scroll to the current location you're editing.
* GitHub Flavored Markdown  
* Syntax highlighting
* [KaTeX](https://khan.github.io/KaTeX/) Support
* Dark/Light mode
* Toolbar for basic Markdown formatting
* Supports multiple cursors
* Save the Markdown preview as PDF
* Emoji support in preview :tada:
* App will keep alive in tray for quick usage
* Full screen mode
  - Write distraction free.
* Cross platform
  - Windows, Mac and Linux ready.
  

![Screenshot](/web_app_image.png?raw=true)


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
