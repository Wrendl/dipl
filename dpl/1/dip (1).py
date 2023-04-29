#!/usr/bin/env python
# coding: utf-8

# In[34]:

#average new (with errors)

prices = []
volume = 2.5
year = 2020
brand = 'Toyota'
model = 'Camry'
fuel_type = 'Бензин'
kpp_type = 'Автомат'
sweel_type = 'Слева'
privod_type = 'Полный'

fuel = {'бензин': 1,
        'дизель':2,
        'газбензин':3,
        'газ':4,
        'гибрид':5,
        'электричество':6}

car_transm = {'механика':1,
              'автомат':2,
              'типтроник':3,
              'вариатор':4,
              'робот':5}

sweel = {'слева':1, 'справа':2}

dwheel = {'передний привод':1, 'передний':1,
          'полный привод': 2, 'полный':2,
          'задний привод':3, 'задний':3}



from bs4 import BeautifulSoup
import requests
import re

host = f'https://kolesa.kz/cars/{brand.lower()}/novye-avtomobili/{model.lower()}/?auto-fuel={fuel[fuel_type.lower()]}&auto-car-transm={car_transm[kpp_type.lower()]}&auto-sweel={sweel[sweel_type.lower()]}&car-dwheel={dwheel[privod_type.lower()]}&auto-car-volume[from]={volume}&auto-car-volume[to]={volume}&year[from]={year}&year[to]={year}'


response = requests.get(host)
soup = BeautifulSoup(response.text, 'html.parser')

items_soup = soup.find_all(class_='a-card__info')

for item in items_soup:
    item_price = re.sub("[^0-9]", "", item.find('span', class_='a-card__price').text)
    prices.append(int(item_price))
    
if len(prices) == 0:
    print('No same')
else:
    print(sum(prices)/len(prices))
    
print(prices)
print(host)


# In[35]:


# s probegom

from bs4 import BeautifulSoup
import requests
import re

prices = []
list1 = []
list2 = []
probeg = 300
radius = 1000

host = f'https://kolesa.kz/cars/{brand.lower()}/avtomobili-s-probegom/{model.lower()}/?auto-fuel={fuel[fuel_type.lower()]}&auto-car-transm={car_transm[kpp_type.lower()]}&auto-sweel={sweel[sweel_type.lower()]}&car-dwheel={dwheel[privod_type.lower()]}&auto-car-volume[from]={volume}&auto-car-volume[to]={volume}&year[from]={year}&year[to]={year}'

response = requests.get(host)
soup = BeautifulSoup(response.text, 'html.parser')

items_soup = soup.find_all(class_='a-card__info')

for item in items_soup:
    item_prob = item.find('p', class_='a-card__description').text
    item_price = item.find('span', class_='a-card__price').text
    if 'с пробегом' in item_prob:
        item_prob = int(re.sub("[^0-9]", "", item_prob[item_prob.find('пробегом') + 8 : item_prob.find('км')]))
        list1.append(item_prob)
        item_price = int(re.sub("[^0-9]", "", item_price))
        prices.append(item_price)
        

while len(list2)==0:
    radius += 1000
    list2 = [x for x in list1 if x in range(probeg-radius, probeg+radius+1)]
    continue
prices = [prices[list1.index(y)] for y in list2]

print(sum(prices)/len(prices))


# In[36]:


from bs4 import BeautifulSoup
import requests
import re
prices = []
brand = 'Nissan'
model = 'Murano'
search = 'Насос гур'

search_str = search.lower().strip().replace(' ', '+')

host = f'https://kolesa.kz/zapchasti/prodazha/{brand.lower()}/{model.lower()}/?_txt_={search_str}&spare-condition=2&has-delivery=1&find-in-text=0'

request1 = requests.get(host)
soup1 = BeautifulSoup(request1.text, 'html.parser')

for i in soup1.find_all(class_='a-card__title'):
    request2 = requests.get('https://kolesa.kz'+ i.find('a', class_='a-card__link')['href']) #item_link
    soup2 = BeautifulSoup(request2.text, 'html.parser')
    
    p = re.sub("[^0-9]", "", soup2.find('div', class_='offer__price').text)
    prices.append(int(p))
    
    
sum(prices[:3])/len(prices[:3])


# In[ ]:




