"""
CreateAdjMat.py

@author : Tappan Ajmera
@author : Sanket Sheth
@author : Rohit Mudaliar
"""

class CreateMat:
    '''
    Contains methods to create adjacency matrix
    '''
    def checkcount(self, single_candidates, word):
        '''
        Checks the count of word in candidate list

        :param single_candidates: list of candidate words
        :param word: single word to check
        :return: number of time the word occurs in the list
        '''
        count = 0
        for w in single_candidates:
            if w == word:
                count = count + 1
        return count

    def checkocc(self,word1, word2, n, candidate,length):
        '''
        Checks co-occurences of the words in the candidate list

        :param word1:
        :param word2:
        :param n: length of candidate list
        :param candidate: candidate list
        :param length:
        :return: count of co-occurence
        '''


        count = 0

        for i in range(length):
            if i + 1 == n:
                break
            if len(candidate[i]) > 1:
                temp = []
                temp = candidate[i].split(" ")
                for i in range(len(temp)):
                    if temp[i] == word1:
                        # new=temp[i:]
                        if (word2 in temp):
                            count = count + 1

        return count

    def graphcreation(self, length_set_single_candidates, single_candidates, combo_words, set_single_candidates):
        '''
        Helper function to create an adjacency matrix
        :param length_set_single_candidates: length of candidate set
        :param single_candidates: single candidates
        :param combo_words: set of combinations of candidates
        :param set_single_candidates: set of single candidates
        :return: matrix
        '''
        setlist = []
        setlist = list(set_single_candidates)
        candidate = combo_words
        length=len(candidate)
        adj = [[0] * length_set_single_candidates for i in range(length_set_single_candidates)]
        for i in range(length_set_single_candidates):
            for j in range(length_set_single_candidates):
                if setlist[i] == setlist[j]:
                    adj[i][j] = self.checkcount(single_candidates, setlist[i])
                else:
                    x = self.checkocc(setlist[i], setlist[j], length_set_single_candidates, candidate, length)
                    adj[i][j] = x

        return adj



    def create_graph_matrix(self, combo_words, single_candidates):
        '''
        Takes input of a list of candidate words and creates an adjacency matrix
        :param combo_words: Candidate list with combination of words
        :param single_candidates: Candidate list with unique words
        :return: Adjacency matrix
        '''

        set_single_candidates = set(single_candidates)
        length_set_single_candidates = len(set_single_candidates)
        return self.graphcreation(length_set_single_candidates, single_candidates, combo_words, set_single_candidates)
