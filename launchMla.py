import json
from os import write
import requests
from selenium import webdriver
#from sheets2 import getSheet
from changeProxy import changeProxy
import time 

listaIds= ['048ecebe-d388-4a59-b623-654176860602', '97c34f62-75d9-4f4d-8ee6-b8355fdbe16e', '40a62d26-787f-46a0-8f9a-776765420615']
#listaGoogle = getSheet()

def launch(id_profile):
    #id_profile = '048ecebe-d388-4a59-b623-654176860602'
    profile_url = 'http://127.0.0.1:35000/api/v1/profile/start?automation=true&profileId='+ id_profile
    resp = requests.get(profile_url)
    print(f'resp.content es {resp.content}')
    j = json.loads(resp.content)
    print(f' la resp es {resp}')
    print(f'j es {j}')
    driver = webdriver.Remote(command_executor=j['value'])
    return driver
#https://app.multiloginapp.com/WhatIsMyIP

"""def main():
    for i in range(1,len(listaGoogle)):
        zip = listaGoogle[i][5]
        changeProxy(zip)
        time.sleep(5)
        driver = launch(listaGoogle[i][4])
        driver.get('https://app.multiloginapp.com/WhatIsMyIP')
        time.sleep(5)
        print("pasaron 10 segundos")
        driver.quit()
        time.sleep(5)"""

#main()
#print(listaGoogle)