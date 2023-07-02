import requests
from bs4 import BeautifulSoup
import json


#BASE_URL='http://search.wanteddistributors.com'
BASE_URL = 'http://search.wanteddistributors.com'


# print(res.status_code)
# print(res.text)

# def get_resp(url):
#     res = requests.get(url)
#     if res.status_code == 200:
#         return res
#     return None


def get_resp(url):
    res = requests.get(url)
    if res.status_code == 200:
      return res
    raise Exception('URL request is not successfull')

    # div(card)
    #     div(card-header)
    #         h4 (card-id) > ID
    #         h3 (card-title) > title
    #     div (card-body)
    #         div(description) 
    #             para > description 
    #         div(poster-info)
    #             para > email  
    #             para > phone number

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
    json_data = json.dumps(l)   
    return json_data

def create_search_url_from_keyword(key):
    url = f"{BASE_URL}/search/?q={key}"
    print(url)
    return url

def get_search_results_from_keyword(keyword):
    url = create_search_url_from_keyword(keyword)
    json_data = get_json_data_from_url(url)
    return json_data


   


   
   
      
   


   
   




if __name__ == '__main__':
    # # http://search.wanteddistributors.com/search/?q=hardware
    # #user_input = input('enter keyword to search :')
    # #url = f"{BASE_URL}/search/?q={user_input}"
    # url = f"{BASE_URL}"
    # print(url)
    # #print(get_resp(url).text)    soup.prettify()
    # # r = get_resp(url).text
    # # #print(r)
    # # soup = BeautifulSoup(r, 'html.parser')
    # # #print(soup.find('div'))


    # # cards = soup.find_all('div',class_='card')
    # # l = []
    # # for card in cards:
    # #    d = create_dic_from_card(card)
    # #    l.append(d)
    # # print(l)

    # print(get_json_data_from_url(url))

    print(get_search_results_from_keyword('FMCG'))







   


    



   


  

















