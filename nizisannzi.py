import requests
import csv
from bs4 import BeautifulSoup

Datas =[]

i = 0

v = requests.get('https://nijisanji.ichikara.co.jp/member/')

member_data = BeautifulSoup(v.text, 'html.parser')

Data_0_0 = member_data.find_all('div',class_="insideline")

def Get_Status(URL):
  global i,Datas

  

  r = requests.get(URL)
  
  HTML_Data = BeautifulSoup(r.text, 'html.parser')
  Data_0 = HTML_Data.find_all('h2',class_="elementor-heading-title elementor-size-default")
  Data_1 = HTML_Data.find_all('div',class_="elementor-social-icons-wrapper")
  
  print('////////////////////////////////////////////////////////////////////////')
  print(Data_0[0].text)
  print(Data_0[1].text)
  
  for datas_1 in Data_1:
    Data_2 = datas_1.find_all('a')
  output =""
  Datas.append( [Data_0[0].text,Data_0[1].text,])
  for datas_2 in Data_2:
    print(datas_2.text)
    print(datas_2.get("href").strip('?sub_confirmation=1'))
    Datas[i].append(datas_2.get("href").replace("?sub_confirmation=1", ""))
  print('////////////////////////////////////////////////////////////////////////')
  print(Datas[i])
  print('===========================================================')
  i +=1


for datas_0 in Data_0_0:
  print(datas_0.a.get("href"))
  Get_Status(datas_0.a.get("href"))
  print(Datas)

with open('nizisanzi.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerows(Datas)
  print('完了')