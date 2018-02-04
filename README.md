# Twitter Conversation Crawler
You can crawl twitter conversations in python3. A conversation consists of 3 tweets.
- Origin tweet by user A
- Reply tweet by user B
- One more reply tweet by user A

This script stores a conversation in sqlite tables (conversation and status table).

## How it works
### Setup

1. Copy the `config.yml.default` to `config.yml`, and fill your twitter application tokens you got from [twitter developers](https://apps.twitter.com/).


2. Then run as follows, please replace en with your language. 
````
% python crawler.py --db conversation.db --lang=en
````

3. Open another terminal and see if you have some conversations stored in the database.
````
% sqlite3 conversation.db
SQLite version 3.13.0 2016-05-18 10:57:30
Enter ".help" for usage hints.
sqlite> select * from conversation limit 1;
960023899768532994|960106507491823616|960118686488162304
sqlite> select * from status where id = 960118686488162304;
...
````
