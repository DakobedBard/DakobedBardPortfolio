package org.mddarr.dakobed.twitterservice.api;


import org.mddarr.dakobed.twitterservice.models.Tweet;
import org.mddarr.dakobed.twitterservice.services.TweetsQueryService;
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
