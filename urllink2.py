from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count=int(input('Enter count:'))
position=int(input('Enter position:'))

retreived=[]

#adding the intial Url into the List of the retrieved URLS
retreived.append(url)

#defining a common function which retrieves the urls present in the anchor tags following the initial Url(or the first Url)
def tags(url,position):
    html=urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    List=[]
    for tag in tags:
        List.append(tag.get('href',None))
    retreived.append(List[position-1])
    return List[position-1]
    List.clear()

for i in range(count+1):
    tags(retreived[i],position)
    print('retreived: ',retreived[i])
