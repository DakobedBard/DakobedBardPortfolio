### Dakobed Twitter Pipeline

I had to use a different maven plugin for this, use the jar-with-dependices.jar instead of the other.  Pass
the hostname & the port of the elasticsearch endpoint.  Will use http for localhost, otherwise will use https

java -jar target/dakobed-twitter-producer-1.0-SNAPSHOT-jar-with-dependencies.jar localhost 29200
