package org.mddarr.dakobedordersservice.producers;

import com.amazonaws.client.builder.AwsClientBuilder;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDB;
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClientBuilder;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapper;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBMapperConfig;
import com.amazonaws.services.dynamodbv2.datamodeling.DynamoDBScanExpression;
import io.confluent.kafka.serializers.AbstractKafkaAvroSerDeConfig;
import io.confluent.kafka.streams.serdes.avro.SpecificAvroSerializer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.common.serialization.StringSerializer;
import org.mddarr.dakobedordersservice.models.ProductDocument;
import org.mddarr.dakobedordersservice.services.ProductAvroService;
import org.mddarr.dakobedordersservice.services.ProductService;
import org.mddarr.products.Product;
import org.mddarr.products.PurchaseEvent;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.DefaultKafkaProducerFactory;
import org.springframework.kafka.core.KafkaTemplate;

import java.util.*;

public class ProductProducer {

    @Autowired
    ProductService productService;

    public static void main(String[] args) throws Exception {
        populateTopics();
    }

    public static List<Product> getProducts(){
        AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard().withEndpointConfiguration(
                new AwsClientBuilder.EndpointConfiguration("http://localhost:8000", "us-west-2"))
                .build();
        DynamoDBMapperConfig mapperConfig = new DynamoDBMapperConfig.Builder().withTableNameOverride(DynamoDBMapperConfig.TableNameOverride.withTableNameReplacement("Dakobed-Products")).build();
        DynamoDBMapper mapper = new DynamoDBMapper(client, mapperConfig);
        DynamoDBScanExpression scanExpression = new DynamoDBScanExpression();
        List <ProductDocument> products = mapper.scan(ProductDocument.class, scanExpression);
        List<Product> products_list = new ArrayList<>();
        for (ProductDocument product: products){
            Product product1 = new Product();
            product1.setBrand(product.getBrand());
            product1.setName(product.getProductName());
            product1.setPrice(product.getPrice());
            product1.setId(product.getId());
            products_list.add(product1);
            System.out.println(product.getProductName());
        }
        return products_list;
    }


    public static void populateTopics() throws Exception{

        final Map<String, String> serdeConfig = Collections.singletonMap(
                AbstractKafkaAvroSerDeConfig.SCHEMA_REGISTRY_URL_CONFIG, "http://localhost:8081");
        // Set serializers and
        final SpecificAvroSerializer<PurchaseEvent> purchaseEventSerializer = new SpecificAvroSerializer<>();
        purchaseEventSerializer.configure(serdeConfig, false);
        final SpecificAvroSerializer<Product> productSerializer = new SpecificAvroSerializer<>();
        productSerializer.configure(serdeConfig, false);

        Map<String, Object> props = new HashMap<>();
        props.put(AbstractKafkaAvroSerDeConfig.SCHEMA_REGISTRY_URL_CONFIG, "http://localhost:8081");
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ProducerConfig.RETRIES_CONFIG, 0);
        props.put(ProducerConfig.BATCH_SIZE_CONFIG, 16384);
        props.put(ProducerConfig.LINGER_MS_CONFIG, 1);
        props.put(ProducerConfig.BUFFER_MEMORY_CONFIG, 33554432);
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, purchaseEventSerializer.getClass());

        Map<String, Object> props1 = new HashMap<>(props);
        props1.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        props1.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, productSerializer.getClass());

        DefaultKafkaProducerFactory<String, Product> pf1 = new DefaultKafkaProducerFactory<>(props1);
        KafkaTemplate<String, Product> template1 = new KafkaTemplate<>(pf1, true);
        template1.setDefaultTopic(ProductAvroService.PRODUCT_FEED);

        List<Product> products = getProducts();

        products.forEach(product -> {
            System.out.println("Writing product information for '" + product.getName() + "' to input topic " +
                    ProductAvroService.PRODUCT_FEED);
            template1.sendDefault(product.getId(), product);
        });

        DefaultKafkaProducerFactory<String, PurchaseEvent> pf = new DefaultKafkaProducerFactory<>(props);
        KafkaTemplate<String, PurchaseEvent> template = new KafkaTemplate<>(pf, true);
        template.setDefaultTopic(ProductAvroService.PURCHASE_EVENTS);

        final long purchase_quantity = 3;
        final Random random = new Random();

        while (true) {
			final Product product = products.get(random.nextInt(products.size()));
			System.out.println("Writing purchase event for product " + product.getName() + " to input topic " + ProductAvroService.PURCHASE_EVENTS);
			template.sendDefault("uk", new PurchaseEvent(1L, product.getId(), purchase_quantity));
			Thread.sleep(100L);
		}
	}
}