### Dakobed Snotel

In this directory I have a data pipeline in which I scrape snowpack and streamflow time series data from the USDA and push 
this data to a DynamoDB table.  This pipeline has been fully dockerized.  

To run the pipeline


docker-compose -f snotel-dynamo-compose.yaml up --build

The range of dates which the scraper runs can be changed in the scrape_snowpack_data() function, at the bottom of the 
snotel.py file.  






