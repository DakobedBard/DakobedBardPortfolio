package org.mddarr.dakobedservices.twitter.api;


import org.mddarr.dakobedservices.twitter.services.TweetsQueryService;
import org.mddarr.dakobedtwitterservice.models.Tweet;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@CrossOrigin
public class TweetsAPI {

    @Autowired
    TweetsQueryService tweetsQueryService;

    @RequestMapping(value = "tweets")
    public List<Tweet> getTweets(){
        return tweetsQueryService.getTweets();
    }

}
