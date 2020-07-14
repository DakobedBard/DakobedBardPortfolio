package org.mddarr.dakobedtwitterservice.dao;

import org.mddarr.dakobedtwitterservice.models.Article;
import org.mddarr.dakobedtwitterservice.models.Tweet;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.elasticsearch.annotations.Query;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface TweetRepository extends ElasticsearchRepository<Tweet, String> {
}