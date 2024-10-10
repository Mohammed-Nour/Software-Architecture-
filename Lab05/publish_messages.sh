#!/bin/bash

# Post 10 messages from the same user (yehia)
for i in {1..10}
do
  curl -X POST http://localhost:5001/post \
  -H "Content-Type: application/json" \
  -d "{\"username\": \"yehia\", \"content\": \"Message number $i\"}"
done

# Fetch the updated feed to confirm all posts were created
curl http://localhost:5001/feed
