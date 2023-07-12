import requests
from bs4 import BeautifulSoup
import json

BASE_URL = 'http://search.wanteddistributors.com'




def get_resp(url):
    res = requests.get(url)
    if res.status_code == 200:
      return res
    raise Exception('URL request is not successfull')



def create_dic_from_card(card):
   d = {}
   card_header = card.find('div',class_='card-header')
   h4 = card_header.find('h4',class_='card-id')
   id = h4.text.split(':')[1]

   h3 = card_header.find('h3',class_='card-title')
   title = h3.text

   card_body = card.find('div',class_='card-body')
   des = card_body.find('div',class_= 'description')
   description = des.text

   poster_info = card_body.find('div',class_='poster-info')
   paras = poster_info.find_all('p')
   email = paras[0].text.split(':')[1].replace(' ','')
   phone = paras[1].text.split(':')[1].strip()

   d['id'] = id
   d['title'] = title
   #d['Description'] = description
   d['email']=email
   d['phone']= phone

   return d

def get_json_data_from_url(url):
    res = get_resp(url)  # we request url and get responce
    soup = BeautifulSoup(res.text, 'html.parser')  # we get bs4 object from response text (html)
    cards = soup.find_all('div',class_='card')
    l = []
    for card in cards:
        d = create_dic_from_card(card)
        l.append(d)
    #json_data = json.dumps(l)   
    #return json_data
    return l

def create_search_url_from_keyword(key):
    url = f"{BASE_URL}/search/?q={key}"
    print(url)
    return url

def get_search_results_from_keyword(keyword):
    url = create_search_url_from_keyword(keyword)
    json_data = get_json_data_from_url(url)
    return json_data


   


   
   
      
   


   
   




if __name__ == '__main__':


    print(get_search_results_from_keyword('FMCG'))



