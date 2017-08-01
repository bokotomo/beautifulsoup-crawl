import urllib.request as urllib
from bs4 import BeautifulSoup

class CrawlWebPage:
  def show(self):
    url = "https://proport.me"
    res = self.get_all_imgs_src(url)
    for v in res:
      print(v)
      print("-------")

  def get_all_imgs_src(self, url):
    '''
    imgタグ一覧からsrcを取得
    '''
    html = urllib.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    res = soup.find_all("img")
    col = []
    for v in res:
      col.append(v["src"])
    return col

