package org.mddarr.dakobedordersservice;

import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapper;
import com.amazonaws.services.dynamodbv2.document.DynamoDB;
import com.amazonaws.services.dynamodbv2.document.Item;
import com.amazonaws.services.dynamodbv2.document.Table;
import com.amazonaws.services.dynamodbv2.model.*;
import com.fasterxml.jackson.core.JsonFactory;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import org.mddarr.dakobedordersservice.dynamo.ProductsTable;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.File;
import java.io.IOException;
import java.util.*;

@SpringBootApplication
public class DakobedProductServiceApplication implements CommandLineRunner {

	@Autowired
	AmazonDynamoDB amazonDynamoDB;

	private DynamoDBMapper dynamoDBMapper;

	private static final Logger logger = LogManager.getLogger(DakobedProductServiceApplication.class);


	public static void main(String[] args) {
		SpringApplication.run(DakobedProductServiceApplication.class, args);
	}

	public Boolean isEmpty(AmazonDynamoDB database, String tableName) {
		ScanRequest scanRequest = new ScanRequest().withTableName(tableName).withLimit(1);
		return database.scan(scanRequest).getScannedCount() == 0;
	}

	@Override
	public void run(String... strings) throws Exception {
		DynamoDB dynamoDB = new DynamoDB(amazonDynamoDB);

		ProductsTable.createProductsTable(dynamoDB);
		if(isEmpty(amazonDynamoDB,"Dakobed-Products")){
			ProductsTable.loadProductsData(dynamoDB);
		}


	}
}


