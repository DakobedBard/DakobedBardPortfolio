FROM openjdk:11-jdk-slim
COPY target/dakobed-twitter-producer-1.0-SNAPSHOT-jar-with-dependencies.jar  app.jar
ENTRYPOINT ["java","-jar","/app.jar", "virus", "elasticsearch7", "29200" ]
# ENTRYPOINT ["java","-jar","/app.jar", "virus", "kafka:9092", "schema-registry:8081"]