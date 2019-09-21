import requests
from bs4 import BeautifulSoup


url = 'https://www.youtube.com/playlist?list=PLnsTUgMW5W__4eI0349Lu64ljXsrRjhwJ' #PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj'
head = {'User-Agent': 'Chrome/50.0.2661.102'}
req = requests.get(url, headers=head)

soup = BeautifulSoup(req.text, "html.parser")

hours = 0
minutes = 0
seconds = 0

timestamps = soup.find_all('span', limit=None)
durations = []

for x in timestamps:
    if ':' in x.text:
        if 7 >= len(x.text) >= 4:
            durations.append(x.text)
print(durations)



'''durations = []


for x in timestamps:
    if len(x.text) <= 5:
        if ':' in x.text:
            durations.append(x.text)

print(len(durations))
 durations = []
for x in timestamps:
    durations.append(x.span.text)


for x in durations:
    if x.count(':') == 1:
        minutes += int(x.split(':')[0])
        seconds += int(x.split(':')[1])
    if x.count(':') == 2:
        hours += int(x.split(':')[0])
        minutes += int(x.split(':')[1])
        seconds += int(x.split(':')[2])

full_hours = 0
full_minutes = 0
full_seconds = hours*3600 + minutes*60 + seconds

full_hours = full_seconds//3600
full_minutes = (full_seconds - (3600*full_hours))//60
full_seconds = (full_seconds - (3600*full_hours) - (full_minutes*60))

print(f'Total Duration of the Playlist is {full_hours} hours, {full_minutes} minutes and {full_seconds} seconds') '''
