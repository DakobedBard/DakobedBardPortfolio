#Dakobed Snotel Service
In this project I scrape streamflow & snowpack data from the USDA.  Initially I was using a postgreSQL database but realized
the relational data model was not appropriate for this data.  For 120 sites within Washington, I am storing six different measurements 
take every day.  I settled with  DynamoDB as it is highly available and allows for efficient queries of the data by the tables hash/primary key which is the LocationID.  
Additionally using the Date as the range/sort key allows for efficient queries on a range of dates.   

### Run the pipeline locally 
docker-compose -f snotel-compose.yaml up --build

### Dakobed Snotel Service Spring Application.  
In order to run the dakobed-snotel-service Spring boot application locally
mvn clean package  -> COMPILE!
java -jar dakobed-snotel-service/target/dakobed-snotel-service-0.0.1-SNAPSHOT.jar


##### Or run using docker 
docker build -t dakobed-snotel-service .

#### Endpoint for getting all data for specific location

localhost:8080/snotel?id=Alpine Meadows

#### Endpoint for getting all data for specific location between dates
curl --request GET localhost:8080/snotel -d 'id=Alpine Meadows&sdate=20140102&edate=20140103'

-> This CURL request doesn't seem to work?  Works from Postman.. 

http://localhost:8080/snotel-dates?id=Elk Butte&sdate=20140102&edate=20140103

### Snotel Elastic Container Registry Commands
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 710339184759.dkr.ecr.us-west-2.amazonaws.com

docker build -t dakobed-snotel-service .

docker tag dakobed-snotel-service:latest 710339184759.dkr.ecr.us-west-2.amazonaws.com/dakobed-snotel-service:latest

docker push 710339184759.dkr.ecr.us-west-2.amazonaws.com/dakobed-snotel-service:latest


