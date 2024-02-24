import json

# access JSON file with webpage data
with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)

'''
extract data based on object labels:
'author' for author of tweet
'date' for date of tweet
'tweet' for text of tweet
'likes' for likes of tweet
'shares' for shares of tweet
'''
for i in jsonData:
    print (i['shares'])