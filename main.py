import urllib.request as urllib
from bs4 import BeautifulSoup

def show():
  url = "http://qiita.com/itkr/items/513318a9b5b92bd56185"
  html = urllib.urlopen(url)
  soup = BeautifulSoup(html)
  res = soup.find_all("a")
  for v in res:
    print(v)
    print("-------")

if __name__ == "__main__":
  show()  
