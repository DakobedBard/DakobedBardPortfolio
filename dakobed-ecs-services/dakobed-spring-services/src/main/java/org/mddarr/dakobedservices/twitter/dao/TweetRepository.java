package org.mddarr.dakobedservices.twitter.dao;

import org.mddarr.dakobedtwitterservice.models.Tweet;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface TweetRepository extends ElasticsearchRepository<Tweet, String> {
}