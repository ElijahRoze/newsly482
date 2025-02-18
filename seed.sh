#!/bin/bash

echo "Seeding application..."
echo "Generating feeds..."

curl -X 'POST' \
  'http://localhost:8000/feed' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feed_url": "https://www.skyandtelescope.com/feed/"
}'

curl -X 'POST' \
  'http://localhost:8000/feed' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feed_url": "https://www.nasa.gov/rss/dyn/breaking_news.rss"
}'

curl -X 'POST' \
  'http://localhost:8000/feed' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feed_url": "http://feeds.macrumors.com/MacRumors-Mac"
}'

curl -X 'POST' \
  'http://localhost:8000/feed' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feed_url": "http://feeds.feedburner.com/osxdaily"
}'

curl -X 'POST' \
  'http://localhost:8000/feed' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feed_url": "https://www.bleedingcool.com/movies/feed/"
}'

curl -X 'POST' \
  'http://localhost:8000/feed' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feed_url": "https://film.avclub.com/rss"
}'

curl -X 'POST' \
  'http://localhost:8000/feed' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feed_url": "https://deadline.com/feed/"
}'

curl -X 'POST' \
  'http://localhost:8000/feed' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feed_url": "https://blog.jetbrains.com/feed"
}'

curl -X 'POST' \
  'http://localhost:8000/feed' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feed_url": "http://feeds.hanselman.com/ScottHanselman"
}'

curl -X 'POST' \
  'http://localhost:8000/feed' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feed_url": "https://hackaday.com/blog/feed/"
}'

curl -X 'POST' \
  'http://localhost:8000/feed' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feed_url": "https://www.ikeahackers.net/feed"
}'

curl -X 'POST' \
  'http://localhost:8000/feed' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "feed_url": "https://bookriot.com/feed/"
}'

echo "Adding users..."

curl -X 'POST' \
  'http://localhost:8000/users/create' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "daniel",
  "password": "daniel"
}'

curl -X 'POST' \
  'http://localhost:8000/users/create' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "elijah",
  "password": "elijah"
}'

echo "Crawling... (this will take a while)"

curl -X 'POST' \
  'http://localhost:8000/crawl' \
  -H 'accept: application/json' \
  -d ''