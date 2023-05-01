
import requests , bs4
from requests import post, get
result=requests.get("https://wallpaperaccess.com/full/266770.jpg")
# soup=bs4.BeautifulSoup(result.text,"lxml")
# first=soup.select('img style')
# print(first)
# print(first.text)
out=result.content

var= open("puppy2.jpg","wb")
var.write(result.content)
var.close()

