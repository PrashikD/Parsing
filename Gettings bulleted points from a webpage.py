import requests
from bs4 import BeautifulSoup

url = 'http://www.ankitfadia.in'  # website of a hacker offering hacking courses
head = {'User-Agent': 'Chrome/50.0.2661.102'}
req = requests.get(url, headers=head)

soup = BeautifulSoup(req.text, "html.parser")

bullets = soup.find('div', class_='modal-body').find_all('li')  # getting the topic names in syllabus

points = [x.text for x in bullets]

print(*points, sep="\n")



