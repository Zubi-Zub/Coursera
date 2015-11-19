#Programs that surf the Web (Chapter 12)

import urllib.request
from bs4 import BeautifulSoup


url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_188301.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup.find_all('span')
commentsTotal = 0
for tag in tags:
	for i in tag:
		if i.isdigit():
			commentsTotal += int(i)
print(commentsTotal)