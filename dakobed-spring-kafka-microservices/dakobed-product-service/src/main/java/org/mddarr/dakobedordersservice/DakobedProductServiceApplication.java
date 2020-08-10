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
import org.apache.kafka.streams.KeyValue;
import org.apache.kafka.streams.kstream.KStream;
import org.apache.kafka.streams.kstream.Materialized;
import org.apache.kafka.streams.kstream.Predicate;
import org.apache.kafka.streams.kstream.TimeWindows;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import org.mddarr.dakobedordersservice.dynamo.ProductsTable;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import java.io.File;
import java.io.IOException;
import java.time.Duration;
import java.util.*;
import java.util.function.Function;

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


	@Bean
	@SuppressWarnings("unchecked")
	public Function<KStream<Object, String>, KStream<?, WordCount>[]> process() {

		Predicate<Object, WordCount> isEnglish = (k, v) -> v.word.equals("english");
		Predicate<Object, WordCount> isFrench =  (k, v) -> v.word.equals("french");
		Predicate<Object, WordCount> isSpanish = (k, v) -> v.word.equals("spanish");

		return input -> input
				.flatMapValues(value -> Arrays.asList(value.toLowerCase().split("\\W+")))
				.groupBy((key, value) -> value)
				.windowedBy(TimeWindows.of(Duration.ofSeconds(6)))
				.count(Materialized.as("WordCounts-1"))
				.toStream()
				.map((key, value) -> new KeyValue<>(null, new WordCount(key.key(), value, new Date(key.window().start()), new Date(key.window().end()))))
				.branch(isEnglish, isFrench, isSpanish);
	}

	static class WordCount {
		private String word;
		private long count;
		private Date start;
		private Date end;
		WordCount(String word, long count, Date start, Date end) {
			this.word = word;
			this.count = count;
			this.start = start;
			this.end = end;
		}
		public String getWord() {
			return word;
		}
		public void setWord(String word) {
			this.word = word;
		}
		public long getCount() {
			return count;
		}
		public void setCount(long count) {
			this.count = count;
		}
		public Date getStart() {
			return start;
		}
		public void setStart(Date start) {
			this.start = start;
		}
		public Date getEnd() {
			return end;
		}
		public void setEnd(Date end) {
			this.end = end;
		}
	}
	@Override
	public void run(String... strings) throws Exception {
//		DynamoDB dynamoDB = new DynamoDB(amazonDynamoDB);
//
//		ProductsTable.createProductsTable(dynamoDB);
//		if(isEmpty(amazonDynamoDB,"Dakobed-Products")){
//			ProductsTable.loadProductsData(dynamoDB);
//		}


	}
}


