from bs4 import BeautifulSoup
import requests
import json

# retrieve all html content for the webpage
url = 'https://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, verify = False, timeout = 5)
content = BeautifulSoup(response.content, "html.parser")

# storing webpage data as JSON element
tweetArr = []
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    # format for data in JSON file
    tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}).text,
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text,
        "tweet": tweet.find('p', attrs={"class": "content"}).text,
        "likes": tweet.find('p', attrs={"class": "likes"}).text,
        "shares": tweet.find('p', attrs={"class": "shares"}).text
    }
    tweetArr.append(tweetObject)

    # saving JSON data as a file
    with open('twitterData.json', 'w') as outfile:
        json.dump(tweetArr, outfile)