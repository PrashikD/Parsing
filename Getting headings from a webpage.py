from bs4 import BeautifulSoup
import requests

url = 'http://www.psychologytoday.com/us/blog/finding-the-next-einstein/201407/seven-ways-be-more-curious'
head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
req = requests.get(url, headers=head)

soup = BeautifulSoup(req.text, "html.parser")

for x in soup.find_all('strong'):
    if x.text[0].isdigit():
        print(x.text)



