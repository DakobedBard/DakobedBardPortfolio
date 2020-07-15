#!/bin/bash
docker exec -it postgres psql 'dbname=snowpackDB user=postgres options=--search_path=snowpack'