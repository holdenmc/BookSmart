import sys
import urllib
import urllib2
import json 
import csv
import re
import os
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
    title = soup.find_all('span', style='font-weight: bold;', class_='textsize3', id=False)[0].text
    for p in soup.find_all('img', src=True):#, href=True, id=True, title=True):
      if 'page' in p.attrs['id']:
        print 'here'
        print p.attrs
        print p.attrs['title']
        ret.add(p.attrs['src'])
      #ret += ' '.join(p.text.encode('utf-8').split())
    return (title, ret)
  except:
    sys.stderr.write("ERROR IN URL: "+url+"\n")
    return set()

if __name__ == '__main__':
  
  st = set()
  for i in range(20):
    '''
    edit here for language link
    '''
    #'http://www.childrenslibrary.org/icdl/SimpleSearchCategory?ids=85&pnum=' + str(i) + '&cnum=1&text=&lang=English&ilangcode=en&ilang=English&langid=315'
    url = 'http://www.childrenslibrary.org/icdl/SimpleSearchCategory?ids=84&pnum=' + str(i) + '&cnum=1&text=&lang=English&ilangcode=en&ilang=English&langid=315'
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
  print len(links)
  for url in links:
    #url = 'http://www.childrenslibrary.org/icdl/BookReader?bookid=carapal_01040002&twoPage=true&route=simple_85_0_0_English_61&size=0&fullscreen=false&pnum1=1&lang=English&ilang=English'
    #url = 'http://www.childrenslibrary.org/icdl/BookReader?bookid=sanelam_00510087&twoPage=false&route=simple_85_0_0_English_61&size=0&fullscreen=false&pnum1=1&lang=English&ilang=English'
    #st = get_image_links('http://www.childrenslibrary.org/icdl/BookReader?bookid=yauaven_00510012&twoPage=false&route=simple_85_0_0_English_61&size=0&fullscreen=false&pnum1=1&lang=English&ilang=English')
    (title, st) = get_image_links(url)
    li = list(st)
    print li[0]
    print li[1]
    print type(li[0])
    print type(str(li[0]))
    reg = re.compile('thumb\d+')


    title = title.replace(" ", '_')
    image_links = [str(link).replace(reg.findall(str(link))[0], 'thumb12') for link in li if 'thumb' in link]
    for i,j in enumerate(image_links):
      print title
      print str(j)
      print str(i)
      if not os.path.exists(title):
        os.makedirs(title)
      urllib.urlretrieve(j, title + '/' + title + '_' + str(i) + ".jpg")

  














