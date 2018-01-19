
<h1 align="center">
  <br>
  <a href="http://www.amitmerchant.com/electron-markdownify"><img src="https://raw.githubusercontent.com/amitmerchant1990/electron-markdownify/master/img/markdownify.png" alt="Markdownify" width="200"></a>
  <br>
  Markdownify
  <br>
</h1>

<h4 align="center">A minimal Markdown Editor desktop app built on top of <a href="http://electron.atom.io" target="_blank">Electron</a>.</h4>

<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a>
  <a href="https://saythanks.io/to/amitmerchant1990">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
<h1 align="center">
  <br>
  Cross-Domain-Recommender-System
  <br>
</h1>
----
## tl;dr
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
  

![screenshot](Cross-Domain-Recommender-System/web_app_image.png)


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
