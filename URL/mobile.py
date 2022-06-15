from tracemalloc import start
import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi"
req = requests.get(url)
content = BeautifulSoup(req.content,'html.parser')
data=content.find_all('div',{class:'_4rR01T'})

links=[]
phn_name=[]
start_link="https://www.filpkart.com"
for items in data
   rest_link=items.find('a')['href']
   name=items.find('div',attrs={'class':'_5THWM1'})
   phn_name.append(name.text)
   link.append(start_link+rest_link)
   
   dataframe={'phone_name':phn_name,'Linls:links'}
   Final_dataframe=pd.DataFrame(dataframe)
   print(Final_dataframe)
Final_dataframe.to_csv('fk_data_url.csv')

