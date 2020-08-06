import findspark
findspark.init()
import pyspark as ps
from pyspark.sql.types import LongType, IntegerType, ArrayType, StringType, BooleanType
from pyspark.ml.clustering import KMeans
import os
import numpy as np
import string
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import CountVectorizer, IDF
from pyspark.sql.functions import udf
import unicodedata
import sys
from pyspark.sql import Row

PUNCTUATION = set(string.punctuation)
STOPWORDS = set(stopwords.words('english'))



def getSparkInstance():
    java8_location= '/usr/lib/jvm/java-8-openjdk-amd64' # Set your own
    os.environ['JAVA_HOME'] = java8_location

    spark = ps.sql.SparkSession.builder \
        .master("local[4]") \
        .appName("individual") \
        .getOrCreate()
    return spark


def create_tweets_dataframe():
    spark = getSparkInstance()

    parquet_files = []
    for folder in os.listdir('tmp'):
        for file in os.listdir('tmp/'+folder):
            parquet_files.append('tmp/{}/{}'.format(folder,file))

    dataframes = []
    for file in parquet_files:
        df = spark.read.parquet(file)
        dataframes.append(df)

    df = dataframes[0]
    for dataf in dataframes[1:]:
        df = df.union(dataf)
    return df


def tokenize(text):
    try:
        regex = re.compile('<.+?>|[^a-zA-Z]')
        clean_txt = regex.sub(' ', text)
        tokens = clean_txt.split()
        lowercased = [t.lower() for t in tokens]
        no_punctuation = []
        for word in lowercased:
            punct_removed = ''.join([letter for letter in word if not letter in PUNCTUATION])
            no_punctuation.append(punct_removed)
        no_stopwords = [w for w in no_punctuation if not w in STOPWORDS]

        STEMMER = PorterStemmer()
        stemmed = [STEMMER.stem(w) for w in no_stopwords]
        return [w for w in stemmed if w]
    except Exception as e:
        return ["failure"]


@udf(returnType=BooleanType())
def find_failed_tokenized_columns(x):
    return True if x == ['failure'] else False


# tokenize_udf = udf(lambda x: tokenize(x), ArrayType(StringType()))
tokenize_udf = udf(lambda x: tokenize(x), ArrayType(StringType()))

df = create_tweets_dataframe()
filtered_dataframe = df.filter(df['content'] != 'null')

tweets_dataframe = filtered_dataframe.select('content', 'date', 'location', 'username')


tokenized_df = df.select('content', tokenize_udf('content').alias('tokenized_content'))
failed_tokenized_df = tokenized_df.select('content','tokenized_content', find_failed_tokenized_columns('tokenized_content').alias('failure'))
null_dataframe = failed_tokenized_df.filter(failed_tokenized_df['failure']=='true')
cv = CountVectorizer(inputCol="content", outputCol="features")
model = cv.fit(df)
result = model.transform(df)
result.show(truncate=False)