package org.mddarr.dakobedservices;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DakobedServicesApplication implements CommandLineRunner {
	@Value("${es_host}")
	String es_host;
	public static void main(String[] args) {
		SpringApplication.run(DakobedServicesApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {
		System.out.println("The ES host is " + es_host);
	}
}
