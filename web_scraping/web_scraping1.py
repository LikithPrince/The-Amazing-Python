

from tkinter import Image
import requests , bs4
from requests import post, get
result=requests.get("https://upload.wikimedia.org/wikipedia/commons/7/75/Alben_Barkley%2C_Vice-President.jpg")
soup=bs4.BeautifulSoup(result.text,"lxml")
first=soup.select('.img')

print(first)
# out=result.content
# for item in first:
#     print(item)
var= Image.open("Alben_Barkley.jpg")
rot=var.transpose(Image.FLIP)

