from bs4 import BeautifulSoup
import requests

url = 'https://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, verify = False, timeout = 5)
content = BeautifulSoup(response.content, "html.parser")
# print(content)
# tweet = content.find('p', attrs={"class": "content"}).text
# print(tweet)

for tweet in content.findAll('p', attrs={"class": "content"}):
    print(tweet.text.encode('utf-8'))