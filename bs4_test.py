import requests

BASE_URL='http://search.wanteddistributors.com'


# print(res.status_code)
# print(res.text)

def get_resp(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res
    return None





if __name__ == '__main__':
   # http://search.wanteddistributors.com/search/?q=hardware
   user_input = input('enter keyword to search :')
   url = f"{BASE_URL}/search/?q={user_input}"
   print(url)
   print(get_resp(url).text)




