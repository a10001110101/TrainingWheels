#Toberdyne Industries April 2020
#toberdyne.net

import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.headless = True
driver =  webdriver.Firefox(options=options)

driver.get('https://primenow.amazon.com/onboard?forceOnboard=1&sourceUrl=%2Fhome')
zip_code = driver.find_element_by_id('lsPostalCode')
zip_code.send_keys("98036")

zip_click = driver.find_element_by_id('a-autoid-1')
zip_click.click()

time.sleep(1)

#Amazon
driver.get('https://primenow.amazon.com/storefront?merchantId=A3IO9LEFI6UFLL&ref_=pn_sf_nav_sbs_2_A3IO9LEFI6UFLL')

status1 = driver.find_element_by_id('nawMessageBox')
print(status1.text +" "+"Amazon")

time.sleep(1)

#Whole Foods
driver.get('https://primenow.amazon.com/storefront?merchantId=A2CY28O5K7ISXT&ref_=pn_sf_nav_sbs_1_A2CY28O5K7ISXT')

status2 = driver.find_element_by_id('nawMessageBox')
print(status2.text +" "+"Whole Foods")

time.sleep(1)

#Bartells
driver.get('https://primenow.amazon.com/storefront?merchantId=A3H17T0B4V7RDA&ref_=pn_sf_nav_sbs_3_A3H17T0B4V7RDA')

status3 = driver.find_element_by_id('nawMessageBox')
print(status3.text +" "+"Bartells")

time.sleep(1)

driver.quit()