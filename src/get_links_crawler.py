import sys
import urllib
import urllib2
import json 
import csv
import re
from bs4 import BeautifulSoup

#http://www.childrenslibrary.org/icdl/SimpleSearchCategory?ids=84&pnum=1&cnum=1&text=&lang=English&ilangcode=en&ilang=English&langid=61
def get_links(url) : 
  """
  This is a method for extracting the text from a url using BeautifulSoup. 

  url- string of the url from which we want to extract text
  """
  try:
    soup = BeautifulSoup(urllib2.urlopen(url).read(), 'html.parser')
    ret = set()
    for p in soup.find_all('a', href=True):
        if '/icdl/BookPreview?bookid=' in p.attrs['href']:
          ret.add(p.attrs['href'])
      #ret += ' '.join(p.text.encode('utf-8').split())
    return ret
  except:
    sys.stderr.write("ERROR IN URL: "+url+"\n")
    return None

def get_read_links(url):
  '''
  gets links to book page
  '''
  try:
    soup = BeautifulSoup(urllib2.urlopen(url).read(), 'html.parser')
    ret = set()
    for p in soup.find_all('a', href=True, id=True):
      if p.attrs['id'] == 'readbook_link':
        ret.add(p.attrs['href'])
      #ret += ' '.join(p.text.encode('utf-8').split())
    return ret
  except:
    sys.stderr.write("ERROR IN URL: "+url+"\n")
    return set()

def get_image_links(url):
  '''
  gets page get_image
  '''
  try:
    soup = BeautifulSoup(urllib2.urlopen(url).read(), 'html.parser')
    ret = set()
    for p in soup.find_all('img', src=True):#, href=True, id=True, title=True):
      if 'page' in p.attrs['id']:
        ret.add(p.attrs['src'])
      #ret += ' '.join(p.text.encode('utf-8').split())
    return ret
  except:
    sys.stderr.write("ERROR IN URL: "+url+"\n")
    return set()

if __name__ == '__main__':
  '''
  st = set()
  for i in range(20):
    url = 'http://www.childrenslibrary.org/icdl/SimpleSearchCategory?ids=84&pnum=' + str(i) + '&cnum=1&text=&lang=English&ilangcode=en&ilang=English&langid=61'
    arr_links = get_links(url)
    st = st | arr_links
  
  links = ['http://www.childrenslibrary.org' + i for i in st]
  st = set()
  for i in links:
    book_links = get_read_links(i)
    st = st | book_links

  links = ['http://www.childrenslibrary.org' + i for i in st]
  print links[0]
  print links[2]
  #arr_links = get_links(url)
  #arr_links = get_links('http://www.childrenslibrary.org/icdl/SimpleSearchCategory?ids=84&pnum=1&cnum=1&text=&lang=English&ilangcode=en&ilang=English&langid=61')
  #print len(arr_links)
  '''
  st = get_image_links('http://www.childrenslibrary.org/icdl/BookReader?bookid=wilwenn_00940123&twoPage=false&route=simple_84_0_0_English_61&size=0&fullscreen=false&pnum1=1&lang=English&ilang=English')
  li = list(st)
  print li[0]
  print li[1]
  print type(li[0])
  print type(str(li[0]))
  reg = re.compile('thumb\d+')


  
  image_links = [str(link).replace(reg.findall(str(link))[0], 'thumb12') for link in li if 'thumb' in link]
  for i,j in enumerate(image_links):
    print str(j)
    print str(i)
    #urllib.urlretrieve(i, str(j) + ".jpg")














