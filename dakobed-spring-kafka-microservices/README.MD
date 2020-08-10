### Dakobed Event Driven Microservices

Microservice for products inventory

### Run the java application locally
mvn clean package
java -jar dakobed-product-service/target/dakobed-product-service-0.0.1-SNAPSHOT.jar 



update-java-alternatives --list

sudo update-java-alternatives --set /usr/lib/jvm/java-1.11.0-openjdk-amd64


docker exec kafka bash bin/kafka-console-consumer.sh --topic words --from-beginning --property print.key=true --bootstrap-server kafka:9092
docker exec kafka bash bin/kafka-console-producer.sh --topic words --from-beginning --property print.key=true --bootstrap-server kafka:9092

