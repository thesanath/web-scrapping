import requests
from bs4 import BeautifulSoup

url="https://summerofcode.withgoogle.com/programs/2022/organizations"

r=requests.get(url)

htmlContent=r.content

soup=BeautifulSoup(htmlContent,'html.parser')

title=soup.title

paras=soup.find_all('p')



print(soup.find('p'))

print(soup.find('p')['class'])


print(soup.find('p').get_text())

print(soup.get_text()) 


anchors=soup.find('a')

all_links=set()

for link in anchors:
    if(link.get('href')!='#'):
        link=add("https://summerofcode.withgoogle.com/programs/2022/organizations"+link.get('href'))
        all_links.add(link)
        print(linkText)







