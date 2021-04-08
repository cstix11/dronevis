# Import Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Open web driver and go to Google Images
driver = webdriver.Chrome('C:/Program Files/chromedriver/chromedriver.exe')
driver.get('https://images.google.com')

# Get search bar and search
box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
box.send_keys('sedan')
box.send_keys(Keys.ENTER)

# Scroll until the end of the webpage
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[4]/div[2]/input').click()
        time.sleep(3)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

for i in range(1, 600):
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[' + str(i) + ']/a[1]/div[1]/img')\
            .screenshot('C:/Users/sherlc/Documents/Coding/TensorFlow/workspace/dronevis/images/civ_vehicle' + str(i) + '.png')
    except:
        pass
