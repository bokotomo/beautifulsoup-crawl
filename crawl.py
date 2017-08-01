import urllib.request as urllib
from bs4 import BeautifulSoup

class CrawlWebPage:
  def __init__(self, url):
    self.html = urllib.urlopen(url)
    self.url = url
    self.soup = BeautifulSoup(self.html, "html.parser")

  def show(self):
    '''
    表示
    '''
    class_name = "clearfix"
    res = self.get_all_class(class_name)
    for v in res:
      print(v)
      print("-------")

  def get_all_class(self, class_name):
    '''
    class一覧からタグ一覧を取得
    '''
    col = []
    res = self.soup.find_all(class_=class_name)
    for v in res:
      col.append(v)
    return col

  def get_all_img_src(self):
    '''
    imgタグ一覧からsrcを取得
    '''
    col = []
    res = self.soup.find_all("img")
    for v in res:
      col.append(v["src"])
    return col

  def get_all_a_href(self):
    '''
    aタグ一覧からhrefを取得
    '''
    col = []
    res = self.soup.find_all("a")
    for v in res:
      col.append(v["href"])
    return col

