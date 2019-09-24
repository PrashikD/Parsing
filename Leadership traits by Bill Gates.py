import requests
from bs4 import BeautifulSoup

url = 'https://www.inc.com/marcel-schwantes/bill-gates-says-this-1-simple-habit-separates-successful-leaders-from-everyone-else.html'  # news article link
head = {'User-Agent': 'Chrome/50.0.2661.102'}
req = requests.get(url, headers=head)

soup = BeautifulSoup(req.text, "html.parser")

points = soup.find_all('div', attrs={'element': 'h2'})

for x in points:
    if not x.text[0].isdigit():
        points.remove(x)

filtered_points = [str(x.text) for x in points]

final_points = [x[3:] for x in filtered_points]

print(*final_points, sep="\n")

''' 
Leadership is not about titles or positional authority. 
Leadership is not about personality traits.
Leadership is not management.
Leadership isn't about you.
Great leaders allow people to fail.
Great leaders create opportunities for people to thrive.
Great leaders embrace respectful disagreement.
Great leaders share leadership.

'''
