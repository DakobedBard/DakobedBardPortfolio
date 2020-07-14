package org.mddarr.dakobed.twitterservice.services;

import org.mddarr.dakobed.twitterservice.dao.TweetRepository;
import org.mddarr.dakobed.twitterservice.models.Tweet;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;


@Service
public class TweetsQueryService {

    @Autowired
    TweetRepository tweetRepository;

    public List<Tweet> getTweets(){
        List<Tweet> tweets = new ArrayList<>();
        tweetRepository.findAll().forEach(tweet -> tweets.add(tweet));
        return tweets;
    }


}
