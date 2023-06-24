import requests

BASE_URL='http://search.wanteddistributors.com'








if __name__ == '__main__':
   # http://search.wanteddistributors.com/search/?q=hardware
   user_input = input('enter keyword to search :')
   url = f"{BASE_URL}/search/?q={user_input}"
   print(url)



   