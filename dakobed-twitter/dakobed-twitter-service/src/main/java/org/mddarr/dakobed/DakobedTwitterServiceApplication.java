package org.mddarr.dakobed;


import org.mddarr.dakobed.twitterservice.dao.ArticleRepository;
import org.mddarr.dakobed.twitterservice.dao.TweetRepository;
import org.mddarr.dakobed.twitterservice.models.Tweet;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

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
