import tweepy
import json
import os

access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('TOKEN_SECRET')
api_key = os.environ.get('API_KEY')
api_key_secret = os.environ.get('API_SECRET_KEY')

auth = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

ghana_woeid = 23424824

trend_result = api.trends_place(ghana_woeid)

for item in trend_result[0]['trends']:
    print(item)
    print( )

# print output in JSON format
trend_result = json.dumps(api.trends_place(ghana_woeid), indent=2)
print(trend_result)


# print tweet containing hashtags
choice = input("Enter Hash_tag: ")
tweets = tweepy.Cursor(api.search, q=choice).items(10)
for tweet in tweets:
    print(tweet.text)
    print( )
