utl = 'https://m.ithome.com/api/news/newslistpageget?Tag=&ot=1574781080000&page=0'
url = 'https://m.ithome.com/api/news/newslistpageget?Tag=&ot=1574768583000&page=1'
import time
print(time.time())
import requests
res = requests.get(url)
print(res.text)
