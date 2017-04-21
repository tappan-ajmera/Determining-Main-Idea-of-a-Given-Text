"""
Code Referred from : http://bdewilde.github.io/blog/2014/09/23/intro-to-automatic-keyphrase-extraction/
@author : Burton DeWilde

Modified by:  Tappan Ajmera, Sanket Sheth, Rohit Mudaliar
"""



import itertools, nltk, string

class CandidateSet:
    '''
    Class contains methods to find out candidate set

    '''

    def extract_combo_candidates(self, text):
        '''
        Extracts candidate list of words which are nouns and adjectives. Takes care of co-occurences.
        :param text: passage
        :return: candidate list
        '''

        good_tags = set(['JJ', 'JJR', 'JJS', 'NN', 'NNP', 'NNS', 'NNPS'])
        punct = set(string.punctuation)
        stop_words = set(nltk.corpus.stopwords.words('english'))
        # tokenize and POS-tag words
        tagged_words = itertools.chain.from_iterable(nltk.pos_tag_sents(nltk.word_tokenize(sent)
                                                                        for sent in nltk.sent_tokenize(text)))
        taggedwords = list(tagged_words)

        i = 0
        candidates = []
        while i < len(taggedwords):
            if taggedwords[i][0].lower() not in stop_words and taggedwords[i][1] in good_tags and not all(
                            char in punct for char in taggedwords[i][0]):
                        candi = taggedwords[i][0].lower()
                        i += 1
                        while i < len(taggedwords) and taggedwords[i][0] not in stop_words:
                            if taggedwords[i][0].lower() not in stop_words and taggedwords[i][1] in good_tags and not all(
                                            char in punct for char in taggedwords[i][0]):
                                candi += " " + taggedwords[i][0].lower()
                                i += 1

                            else:
                                break
                        candidates.append(candi)
            i += 1
        return candidates

    def extract_single_candidate(self, text):
        '''
        Extracts candidate list of words which are nouns and adjectives.
        :param text: passage
        :return: candidate list
        '''

        good_tags = set(['JJ', 'JJR', 'JJS', 'NN', 'NNP', 'NNS', 'NNPS'])
        # exclude candidates that are stop words or entirely punctuation
        punct = set(string.punctuation)
        stop_words = set(nltk.corpus.stopwords.words('english'))
        # tokenize and POS-tag words
        tagged_words = itertools.chain.from_iterable(nltk.pos_tag_sents(nltk.word_tokenize(sent)
                                                                        for sent in nltk.sent_tokenize(text)))

        # filter on certain POS tags and lowercase all words
        candidates = [word.lower() for word, tag in tagged_words
                      if tag in good_tags and word.lower() not in stop_words
                      and not all(char in punct for char in word)]

        return candidates