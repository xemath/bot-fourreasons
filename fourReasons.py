import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from sheetFourReasons import getSheet, writeSheet, getEmails
from launchMla import launch
import time
from changeProxy import changeProxy

arrayProducts = getSheet()
arrayEmails = getEmails()
array = ["Color Mask Pearl","Color Mask Champagne","Color Mask Silver","Color Mask Red",
"Color Mask Bronze",
"Color Mask Mahogany",
"Color Mask Copper",
"Color Mask Caramel",
"Color Mask Apricot",
"Color Mask Chocolate",
"Color Mask Latte",
"Color Mask Graphite",
"Color Mask Toffee",
"Color Mask Plum",
"Color Mask Coffee",
"Color Mask Vanilla",
"Color Mask Rose Gold",
"Color Mask Rose",
"Color Mask Shampoo Red",
"Color Mask Shampoo Bronze",
"Color Mask Shampoo Chocolate",
"Color Mask Shampoo Pearl",
"Color Mask Shampoo Platinum",
"Color Mask Red Copper",
"Color Mask Shampoo Rose Pink",
"Color Mask Shampoo Rose Gold"] 
#array = ["Color Mask Shampoo Rose Gold","Color Mask Shampoo Rose Pink"]

def main(array):
    indexArray = 0
    productsCount = 0
    indexArrayEmail = 0
    indexEmailsGoogle = 2
    print(f'el item que voy a usar es{array[indexArray][0]}')
    while True:
        if array[indexArray][0] == "Color Mask Champagne" or array[indexArray][3]=="-":
            indexArray = indexArray + 1
            continue
        #driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        changeProxy(arrayEmails[indexArrayEmail][11])
        time.sleep(1)
        driver = launch(arrayEmails[indexEmailsGoogle][0])
        print(array[indexArray][0])
        driver.get('https://www.fourreasons.us/')
        driver.maximize_window()
        #time.sleep(5)
        print('durmiendo')
        try:
            closeButton = driver.find_element_by_xpath('/html/body/div[5]/div/a')
            closeButton.click()
            driver.get('https://www.fourreasons.us/collections/shop')

        except:
            driver.get('https://www.fourreasons.us/collections/shop')
        print('Paso del inicio')


        print('estamos en la tienda!')
        try:
            elemento = driver.find_element_by_partial_link_text(array[indexArray][0])
            elemento.click()
            

            
        except:
            driver.get('https://www.fourreasons.us/collections/shop/color-mask?page=2')
            elemento = driver.find_element_by_partial_link_text(array[indexArray][0])
            elemento.click()
            
        writeSheet([[driver.current_url.split('?')[0]]], f'N{indexEmailsGoogle}')
        time.sleep(2)
        addToCarButton = driver.find_element_by_id('add-to-cart')
        addToCarButton.click()

        time.sleep(10)
        try:
            closeButton = driver.find_element_by_xpath('/html/body/div[7]/div/a')
            closeButton.click()
            time.sleep(1)
            checkOutButton = driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[2]/div/div[3]/div/div[2]/button')
            checkOutButton.click()
        except:
            checkOutButton = driver.find_element_by_xpath('/html/body/div[1]/div[1]/form/div[2]/div/div[3]/div/div[2]/button')
            checkOutButton.click()
        
        reductionCode = driver.find_element_by_id('checkout_reduction_code')
        reductionCode.send_keys('creviews')
        applyButton = driver.find_element_by_xpath('//*[@id="order-summary"]/div/div[2]/form[2]/div/div/div/button')
        applyButton.click()
        time.sleep(2)
        print('funciona')
        #empieza entrada de datos
        try:
            contact_information_input = driver.find_element_by_id('checkout_email_or_phone')
            contact_information_input.send_keys(arrayEmails[indexArrayEmail][1])

            first_name = driver.find_element_by_id('checkout_shipping_address_first_name')
            first_name.send_keys(arrayEmails[indexArrayEmail][5])

            last_name = driver.find_element_by_id('checkout_shipping_address_last_name')
            last_name.send_keys(arrayEmails[indexArrayEmail][6])

            addres = driver.find_element_by_id('checkout_shipping_address_address1')
            addres.send_keys(arrayEmails[indexArrayEmail][7])

            city = driver.find_element_by_id('checkout_shipping_address_city')
            city.send_keys(arrayEmails[indexArrayEmail][9])

            select_country = Select(driver.find_element_by_id('checkout_shipping_address_country'))
            select_country.select_by_value("United States")

            select_province = Select(driver.find_element_by_id('checkout_shipping_address_province'))
            select_province.select_by_value(arrayEmails[indexArrayEmail][10])

            

            zip_code_input = driver.find_element_by_id('checkout_shipping_address_zip')
            zip_code_input.send_keys(arrayEmails[indexArrayEmail][11])
        except:
            writeSheet([['Error']], f'O{indexEmailsGoogle}')
            productsCount = productsCount + 1
            indexArrayEmail = indexArrayEmail + 1
            indexEmailsGoogle = indexEmailsGoogle + 1
            indexArray = indexArray + 1
            driver.quit()
            continue
        #finaliza entrada de datos
        continue_button = driver.find_element_by_id('continue_button')
        continue_button.click()
        #
        continue_button_two = driver.find_element_by_id('continue_button')
        continue_button_two.click()

        writeSheet([['Success']], f'O{indexEmailsGoogle}')
        
        productsCount = productsCount + 1
        indexArrayEmail = indexArrayEmail + 1
        indexEmailsGoogle = indexEmailsGoogle + 1
        print(f'index del array de productos es {indexArray}, el producto es {array[indexArray][0]}, el numero de productos es {int(array[indexArray][3])} y la cuenta va en {productsCount}')
        if productsCount == int(array[indexArray][3]):
            productsCount = 0
            indexArray = indexArray + 1 
            print("entro al if")
        driver.quit()
        if indexArrayEmail==len(arrayEmails):
            break
        time.sleep(5)
main(arrayProducts)
#print(arrayProducts)