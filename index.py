# Written by Salih Hasan & Sameed Hayat
import sys,os,json
import numpy as np
import csv
import urlparse
from optparse import OptionParser
from BaseHTTPServer import HTTPServer,BaseHTTPRequestHandler
from BaseHTTPServer import HTTPServer


def read_uris_from_csv(path_to_csv):
    """
    read all uris from csv
    @param path_to_csv: path to csv file
    @return: list of all the uris
    """
    ret = []
    with open(path_to_csv) as csv_file:
        data = csv.reader(csv_file, delimiter=' ')
        for row in data:
            ret.append(row[0])
    return ret


def write_uris_to_csv(uris):
    """
    write uris to csv for autocomplete
    @param uris: list of all the uris in the input csv file
    @return: nothing
    """
    with open("output", "wb") as csv_file:
            print(len(uris))
            for i, u in enumerate(uris):
                uri = uris[i].replace("http://dbpedia.org/resource/", "").replace("_", " ")
                csv_file.write('"{}",'.format(uri))
    return 0


def get_uri_index(uri, uris):
    """
    get uri index from all the uris
    @param uri: uri to be searched
    @param uris: list of all the uris
    @return: index of the uri
    """
    for i, u in enumerate(uris):
        if u == uri:
            return i


def get_uris_from_index(uris, index_list):
    """
    get multiple uris defined by multiple indexes
    @param uris: list of all the uris
    @param index_list: indexes to be searched
    @return: formatted list of all the uris given by uri index
    """
    return [uris[i].replace("http://dbpedia.org/resource/","").replace("_"," ") for i in index_list]


def top_k_recommendations(index, similarity_matrix, n):
    """
    get multiple uris defined by multiple indexes
    @param index: index of uri in the similarity matrix
    @param similarity_matrix: similarity matrix
    @param n: top n from the list
    @return: formatted list of all the uris given by uri index
    """
    return similarity_matrix[index,:].argsort()[-n:][::-1]


def print_usage():
    print('Usage: index.py -m <modelfile> [-b]')


class HttpServer:
    """
    start HttpServer at the given port + invoke Http handler
    """
    def __init__(self, port, doc_uris_movie, doc_uris_book, rdf_uris_movie, rdf_uris_book,
                 doc_cross_similarity_matrix, rdf_cross_similarity_matrix, doc_movie_similarity_matrix,
                 rdf_movie_similarity_matrix):
        def handler(*args):
            WordAndDoc2VecHandler(doc_uris_movie, doc_uris_book, rdf_uris_movie, rdf_uris_book,
                                  doc_cross_similarity_matrix, rdf_cross_similarity_matrix, doc_movie_similarity_matrix,
                                  rdf_movie_similarity_matrix, * args)
        server = HTTPServer(('', port), handler)
        print('Starting server at port {}, use <Ctrl-C> to stop').format(port)
        server.serve_forever()


class WordAndDoc2VecHandler(BaseHTTPRequestHandler):
    """
    Http GET request handler class
    """
    def __init__(self, doc_uris_movie, doc_uris_book, rdf_uris_movie, rdf_uris_book,
                 doc_cross_similarity_matrix, rdf_cross_similarity_matrix, doc_movie_similarity_matrix,
                 rdf_movie_similarity_matrix, *args):
        self.doc_uris_movie = doc_uris_movie
        self.doc_uris_book = doc_uris_book
        self.rdf_uris_movies = rdf_uris_movie
        self.rdf_uris_book = rdf_uris_book
        self.doc_cross_similarity_matrix = doc_cross_similarity_matrix
        self.doc_movie_similarity_matrix = doc_movie_similarity_matrix
        self.rdf_cross_similarity_matrix = rdf_cross_similarity_matrix
        self.rdf_movie_similarity_matrix = rdf_movie_similarity_matrix
        BaseHTTPRequestHandler.__init__(self, *args)

    def jsonResponse(self,content):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(content))

    def do_GET(self):
        try:
            if self.path.startswith('/recommender'):
                word = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('recommender_word', None)[0]
                original_word = word
                uri = "http://dbpedia.org/resource/" + word.replace(" ","_")
                k=15
                ind = get_uri_index(uri, self.doc_uris_movie)
                uris_ind = top_k_recommendations(ind, self.doc_cross_similarity_matrix, k)
                web_uris = get_uris_from_index(self.doc_uris_book, uris_ind)
                if original_word in web_uris:
                    web_uris.remove(original_word)
                self.jsonResponse(web_uris)
                return
            elif self.path.startswith('/recommend_movie'):
                word = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('movie_recommend', None)[0]
                original_word = word
                uri = "http://dbpedia.org/resource/" + word.replace(" ","_")
                print(uri)
                k=15
                ind = get_uri_index(uri, self.rdf_uris_movies)
                uris_ind = top_k_recommendations(ind, self.doc_movie_similarity_matrix, k)
                web_uris = get_uris_from_index(self.rdf_uris_movies, uris_ind)
                if original_word in web_uris:
                    web_uris.remove(original_word)
                self.jsonResponse(web_uris)
                return
            elif self.path.startswith('/recommend_rdf_movie'):
                word = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('rdf_movie_recommend', None)[0]
                original_word = word
                uri = "http://dbpedia.org/resource/" + word.replace(" ","_")
                print(uri)
                k=15
                ind = get_uri_index(uri, self.rdf_uris_movies)
                uris_ind = top_k_recommendations(ind, self.rdf_movie_similarity_matrix, k)
                web_uris = get_uris_from_index(self.rdf_uris_movies, uris_ind)
                if original_word in web_uris:
                    web_uris.remove(original_word)
                self.jsonResponse(web_uris)
                return
            elif self.path.startswith('/cdrs'):
                word = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('sim_word', None)[0]
                original_word = word
                uri = "http://dbpedia.org/resource/" + word.replace(" ", "_")
                print(uri)
                k = 15
                ind = get_uri_index(uri, self.rdf_uris_movies)
                uris_ind = top_k_recommendations(ind, (0.3 * self.doc_cross_similarity_matrix
                                                       + 0.7 * self.rdf_cross_similarity_matrix), k)
                web_uris = get_uris_from_index(self.rdf_uris_book,uris_ind)
                if original_word in web_uris:
                    web_uris.remove(original_word)
                self.jsonResponse(web_uris)
                return
            elif self.path == '/':
                f = open('index.html')
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
        except IOError:
            self.send_error(404, 'file not found')


def main(argv):
    parser = OptionParser()
    parser.add_option("-p", "--port",
                      type="int", dest="port", default=8080,
                      help="server port")
    (options, args) = parser.parse_args()

    path_to_doc_movie_csv = "doc2vecMovieEmbeddings.csv"
    path_to_doc_book_csv = "doc2vecBookEmbeddings.csv"

    doc_uris_movie = read_uris_from_csv(path_to_doc_movie_csv)
    doc_uris_book = read_uris_from_csv(path_to_doc_book_csv)

    path_to_rdf_movie_csv = "rdf2vecMovieEmbeddings.csv"
    path_to_rdf_book_csv = "rdf2vecBookEmbeddings.csv"

    rdf_uris_movie = read_uris_from_csv(path_to_rdf_movie_csv)
    rdf_uris_book = read_uris_from_csv(path_to_rdf_book_csv)

    doc_movie_embeddings = np.loadtxt(path_to_doc_movie_csv, delimiter=' ', usecols=range(1, 201))
    doc_book_embeddings = np.loadtxt(path_to_doc_book_csv, delimiter=' ', usecols=range(1, 201))

    rdf_movie_embeddings = np.loadtxt(path_to_rdf_movie_csv, delimiter=' ', usecols=range(1, 201))
    rdf_book_embeddings = np.loadtxt(path_to_rdf_book_csv, delimiter=' ', usecols=range(1, 201))

    doc_cross_similarity_matrix = np.dot(doc_movie_embeddings, doc_book_embeddings.T)
    doc_movie_similarity_matrix = np.dot(doc_movie_embeddings, doc_movie_embeddings.T)

    rdf_cross_similarity_matrix = np.dot(rdf_movie_embeddings, rdf_book_embeddings.T)
    rdf_movie_similarity_matrix = np.dot(rdf_movie_embeddings, rdf_movie_embeddings.T)

    HttpServer(options.port, doc_uris_movie, doc_uris_book, rdf_uris_movie, rdf_uris_book,
               doc_cross_similarity_matrix, rdf_cross_similarity_matrix, doc_movie_similarity_matrix,
               rdf_movie_similarity_matrix)


if __name__ == "__main__":
    main(sys.argv[1:])
