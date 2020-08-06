import findspark
findspark.init()
import pyspark as ps
from pyspark.sql.functions import udf
from pyspark.sql.types import LongType, IntegerType, ArrayType, StringType
from pyspark.ml.clustering import KMeans

import os
import re

import numpy as np
import string
import re

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import CountVectorizer, IDF
from pyspark.sql.functions import udf

from pyspark.sql import Row

PUNCTUATION = set(string.punctuation)
STOPWORDS = set(stopwords.words('english'))


from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.util import ngrams
from nltk import pos_tag
from nltk import RegexpParser

from pyspark.ml.feature import CountVectorizer
import unicodedata
import sys

def extract_bow_from_raw_text(text_as_string):
    """Extracts bag-of-words from a raw text string.
    Parameters
    ----------
    text (str): a text document given as a string
    Returns
    -------
    list : the list of the tokens extracted and filtered from the text
    """
    if (text_as_string == None):
        return []
    if (len(text_as_string) < 1):
        return []
    if sys.version_info[0] < 3:
        nfkd_form = unicodedata.normalize('NFKD', unicode(text_as_string))
    else:
        nfkd_form = unicodedata.normalize('NFKD', str(text_as_string))
    text_input = str(nfkd_form.encode('ASCII', 'ignore'))
    sent_tokens = sent_tokenize(text_input)
    tokens = list(map(word_tokenize, sent_tokens))
    sent_tags = list(map(pos_tag, tokens))
    grammar = r"""
        SENT: {<(J|N).*>}                # chunk sequences of proper nouns
    """

    cp = RegexpParser(grammar)
    ret_tokens = list()
    stemmer_snowball = SnowballStemmer('english')

    for sent in sent_tags:
        tree = cp.parse(sent)
        for subtree in tree.subtrees():
            if subtree.label() == 'SENT':
                t_tokenlist = [tpos[0].lower() for tpos in subtree.leaves()]
                t_tokens_stemsnowball = list(map(stemmer_snowball.stem, t_tokenlist))
                #t_token = "-".join(t_tokens_stemsnowball)
                #ret_tokens.append(t_token)
                ret_tokens.extend(t_tokens_stemsnowball)
            #if subtree.label() == 'V2V': print(subtree)
    #tokens_lower = [map(string.lower, sent) for sent in tokens]

    return(ret_tokens)