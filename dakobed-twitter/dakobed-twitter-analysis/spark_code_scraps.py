@udf(returnType=ArrayType(StringType()))
def tokenize_column(x):
    return tokenize(x)