import requests
from bs4 import BeautifulSoup

#BASE_URL='http://search.wanteddistributors.com'
BASE_URL = 'http://search.wanteddistributors.com/search/?q=hardware'


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
    return None


   
   




if __name__ == '__main__':
    # http://search.wanteddistributors.com/search/?q=hardware
    #user_input = input('enter keyword to search :')
    #url = f"{BASE_URL}/search/?q={user_input}"
    url = f"{BASE_URL}"
    print(url)
    #print(get_resp(url).text)    soup.prettify()
    r = get_resp(url).text
    #print(r)
    soup = BeautifulSoup(r, 'html.parser')
    #print(soup.find('div'))

    h4_tag = soup.find_all("h4",class_= "card-id")
    id_no = [i.text for i in h4_tag]






    h3_tag = soup.find_all('h3',class_="card-title")
    titles = [i.text for i in h3_tag]
    # for i in title:
    #    print(i)



    divs = soup.find_all('div',class_="poster-info")
    contacts = [i.text for i in divs]
    #print(contacts)
    # for i in contacts:
    #    print(i)



    file_dis = 'distributors.txt'
    with open(file_dis, 'w') as file:
       for id,title,contact in zip(id_no, titles, contacts):
          file.write(f"{id},{title},{contact}" '\n' )

    


    # for i in values:
    #    print(i)

   


  

















