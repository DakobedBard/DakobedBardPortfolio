spark = getSparkInstance()
sc = spark.sparkContext
hc = ps.HiveContext(sc)

df = hc.createDataFrame([
    (0, "PYTHON HIVE HIVE".split(" ")),
    (1, "JAVA JAVA SQL".split(" "))
], ["id", "words"])

df.show(truncate = False)