from hashlib import md5
from time import time
from requests import post,get
import datetime

m = md5()
m.update(str(time()).encode(encoding='UTF-8'))
uuid = m.hexdigest()
api = 'http://ihealth.hq.gench.edu.cn/api/GDaily/add'
data = {
    'type': '学生',
    'uuid': uuid,
    'userid': '1623228',
    'username': '丁伟',
    'collegename': '信息技术学院',
    'classname': '计科智能B16-3',
    'phone': '15579760328',
    'slocationcode': '360000',
    'slocation': '江西省',
    'locationcode': '360000',
    'location': '赣州市',
    'fever': '0',
    'symptomids': '[]',
    'diagnosis': '0',
    'touchquezhen': '0',
}
cookies = {
    'gench_hq_user': 'eSjHa2RgN+ocTBhxiv0vcQ=='
}

res = post(url=api, data=data, cookies=cookies)
with open('./hhh','a',encoding='utf-8') as f:
    f.writelines(str(datetime.datetime.now())+str(res.json())+'\n')
# if res.json().get('suc')==True:
#     url = 'https://api.day.app/EZLfNsbV6JPoFGXtdEjdp4/打卡/打卡成功'
#     res = get(url)

# print(datetime.datetime.now())
# url = 'https://api.day.app/EZLfNsbV6JPoFGXtdEjdp4/打卡/打卡成功'
# res = get(url)
