import findspark
findspark.init()
import pyspark as ps
from pyspark.sql.functions import udf
from pyspark.sql.types import LongType, IntegerType, ArrayType
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import CountVectorizer
import os


def getSparkInstance():
    java8_location= '/usr/lib/jvm/java-8-openjdk-amd64' # Set your own
    os.environ['JAVA_HOME'] = java8_location

    spark = ps.sql.SparkSession.builder \
        .master("local[4]") \
        .appName("individual") \
        .getOrCreate()
    return spark



# You'll need to use the .fit() method of the CountVectorizer object and the .transform() method of the model object returned by .fit().
# CountVectorizer will select the top VocabSize words ordered by term frequency. The model will produce a sparse vector which can be fed into other algorithms.

@udf(returnType=IntegerType())
def add_one(x):
    if x is not None:
        return x + 1


spark = getSparkInstance()
sc = spark.sparkContext
hc = ps.HiveContext(sc)

df = hc.createDataFrame([
    (0, "PYTHON HIVE HIVE".split(" ")),
    (1, "JAVA JAVA SQL".split(" "))
], ["id", "words"])

df.show(truncate = False)


# CountVectorizer will select the top VocabSize words ordered by term frequency. The model will produce a sparse vector which can be fed into other algorithms.
cv = CountVectorizer(inputCol="words", outputCol="features")
model = cv.fit(df)
result = model.transform(df)
result.show(truncate=False)