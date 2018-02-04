# Twitter Conversation Crawler
You can crawl twitter conversations in python3. A conversation consists of 3 tweets.
- Origin tweet by user A
- Reply tweet by user B
- One more reply tweet by user A

This script stores a conversation in sqlite tables (conversation and status table).

## How it works
### Setup

1. Copy the `config.yml.default` to `config.yml`, and fill your twitter application tokens you got from [twitter developers](https://apps.twitter.com/).


2. Then run as follows, please replace [en] with your language. 
````
% python twitter_conversations.py --db conversation.db --lang=[en]
````
