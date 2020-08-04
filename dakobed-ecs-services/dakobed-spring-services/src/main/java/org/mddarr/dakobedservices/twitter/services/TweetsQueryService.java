package org.mddarr.dakobedservices.twitter.services;


import org.mddarr.dakobedservices.twitter.dao.TweetRepository;
import org.mddarr.dakobedtwitterservice.models.Tweet;
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
