I am practicing some data engineering concepts here 

flighs pipleline will be what I work on first.  

I was able to check for the existance of someting in the dataframes array field.  This was done using

from pyspark.sql import functions as F
containsRestaurants = FiveStarsPheonixCC.filter(array_contains(F.col("categories"), "Food"))

For some reason the col method does not want to get imported nicely in PyCharm. 


- Write parquet files to an S3 bucket.  


Use ipyspark instead of pyspark or else some of the classes will not be found 




THe WITH keyword in python is used when working with unmanaged resources (such as file streams).  Ensures that a 
resource is "cleaned up" when the code that uses it finishes running, even if an exception is thrown.  
Porvides syntactic sugar for 'try/finally' blocks

The with statement clarifies code that previously would use try...finally blocks to ensure that clean-up code is executed. In this section, I’ll discuss the statement as it will commonly be used. In the next section, I’ll examine the implementation details and show how to write objects for use with this statement.