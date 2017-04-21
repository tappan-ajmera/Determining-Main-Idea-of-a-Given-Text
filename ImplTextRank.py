"""
Code referred from
https://joshbohde.com/blog/document-summarization
@author : Josh Bohde

Modified by:  Tappan Ajmera, Sanket Sheth, Rohit Mudaliar

"""


import networkx as nx
from sklearn.feature_extraction.text import TfidfTransformer




class Rankwords:
    '''


    '''
    def find_ranks(self, mat, words):
        '''
        Calls sklearn TfIdf transform to create a tfidf matrix and then convert it to graph using networkx module
        :param mat: Adjacency matrix of candidate words
        :param words: unique candidate words
        :return: Word list with their rank
        '''

        normalized = TfidfTransformer().fit_transform(mat)
        similarity_graph = normalized * normalized.T
        nx_graph = nx.from_scipy_sparse_matrix(similarity_graph)
        scores = nx.pagerank(nx_graph)
        return sorted(((scores[i], s) for i, s in enumerate(words)),
                     reverse=True)