tokenize_udf = udf(lambda x: tokenize(x), ArrayType(StringType()))

@udf(returnType=ArrayType(StringType()))
def tokenize_column(x):
    return tokenize(x)