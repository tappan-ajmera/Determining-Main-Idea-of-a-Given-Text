"""
ExtractKeywords.py

@author : Tappan Ajmera
@author : Sanket Sheth
@author : Rohit Mudaliar
"""


from CandidateSetModule import CandidateSet
from CreateAdjMat import CreateMat
from ImplTextRank import Rankwords



class GetKeyWords:
    """
    The methods in this class are used to find out the keywords in a given text

    """
    def keyword_rank(self, text):
        '''
        The following method takes the given text, finds a list of candidate words, creates an adjacency matrix
        and passes it to page rank algorithm to find out final scores of the words in a given text.

        :param text: Text whose score is to be calculated
        :return: A list of top 5 words
        '''

        cand_set = CandidateSet()
        cand_mat = CreateMat()
        text_rank = Rankwords()

        # split the text by lines
        text = ' '.join(text.strip().split('\n'))


        #Find candidate word list which can contain a phrase depending upon co-occurence of the words
        combo = cand_set.extract_combo_candidates(text)


        #Find candidate word list where all words are added idividually

        words = cand_set.extract_single_candidate(text)

        #Create an adjacency matrix for the given candidate words
        mat = cand_mat.create_graph_matrix(combo, words)


        #Rank words depending upon its importance. Highest-Lowest
        keywords = text_rank.find_ranks(mat, set(words))
        dict_scores = {}
        #print(keywords)
        #Create a lookup dictionary. word:score
        for tup in keywords:
            dict_scores[tup[1]] = tup[0]

        '''
        Create a list to handle the final set of best words. This list is created on the basis of co-occurence.
        For eg:
        Linear diaophantine equations :
        In the above given phrase, there are no stop words or non-noun , non-adjectives between them so they can be
        considered as one entity. So we add scores of all three of them and store in this list.
        '''
        finalSet = []

        for word in keywords[0:5]:
            for string in combo:
                temp = string.split(" ")
                if word[1] in temp:
                    score = 0
                    for w in temp:
                        score += dict_scores[w]
                    if self.check_not_list(temp,finalSet):
                        finalSet.append((score,temp))

        return sorted(finalSet,reverse=True)


    def check_not_list(self,word,list):
        '''
        Check if the combination is already added in the final list
        :param word: combination to be checked
        :param list: final list
        :return: boolean value
        '''

        for item in list:
            if word == item[1]:
                return False

        return True


    def extract_keywords(self):
        '''
        Takes input as a text file and print keywords
        :return: none
        '''

        textFile = input("Please input file name:")
        passage=''
        try:
            with open(textFile) as tf:
                for line in tf:
                    passage += line
        except:
            print("Please enter a valid file name")
            exit()
        keyWords = GetKeyWords().keyword_rank(passage)
        print("Top words are:")
        for word in keyWords[0:5]:
            final_word = ''
            for part in word[1]:
                final_word += " " + part
            print(final_word)

if __name__ == "__main__":

    startExtraction = GetKeyWords()
    startExtraction.extract_keywords()
