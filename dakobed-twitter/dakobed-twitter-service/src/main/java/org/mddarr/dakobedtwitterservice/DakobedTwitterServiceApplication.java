package org.mddarr.dakobedtwitterservice;


import org.mddarr.dakobedtwitterservice.dao.ArticleRepository;
import org.mddarr.dakobedtwitterservice.dao.TweetRepository;
import org.mddarr.dakobedtwitterservice.models.Article;
import org.mddarr.dakobedtwitterservice.models.Author;
import org.mddarr.dakobedtwitterservice.models.Tweet;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.ArrayList;
import java.util.List;

@SpringBootApplication
public class DakobedTwitterServiceApplication implements CommandLineRunner {

	@Autowired
	ArticleRepository articleRepository;

	@Autowired
	TweetRepository tweetsRepository;

	public static void main(String[] args) {
		SpringApplication.run(DakobedTwitterServiceApplication.class, args);
	}

	@Override
	public void run(String... args) throws Exception {

		Tweet tweet = new Tweet();
		tweet.setContent("Virus is whack");
		tweet.setUsername("Tucker1");
		tweet.setLocation("Seattle");
		tweetsRepository.save(tweet);

	}
}
