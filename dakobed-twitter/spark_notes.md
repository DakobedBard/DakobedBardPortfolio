Start the master server..

$SPARK_HOME/sbin/start-master.sh

http://127.0.0.1:8080/

$SPARK_HOME/bin/spark-submit first_spark_submit_job.py

$SPARK_HOME/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8:2.4.6


Spark requires Java 8

List java versions

sudo update-java-alternatives --set /usr/lib/jvm/java-1.8.0-openjdk-amd64
/usr/lib/jvm/java-1.11.0-openjdk-amd64
/usr/lib/jvm/java-1.8.0-openjdk-amd64