package org.mddarr.dakobed.twitterservice.dao;

import org.mddarr.dakobed.twitterservice.models.Tweet;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface TweetRepository extends ElasticsearchRepository<Tweet, String> {
}