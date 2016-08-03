

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

from bs4 import BeautifulSoup
html = urlopen('http://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(html)
titles = soup.find_all("a", "title")

for title in titles:
    print('title:{0:10s} link:{1:20s}\n'.format(title['title'], title['href']))
