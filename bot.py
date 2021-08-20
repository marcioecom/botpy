from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Credentials
url = "https://www.nimo.tv/"
number = "123456789"
password = "password" 
text_msg = "Text example"

# Init Browser
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(url)

# Click in Login button
browser.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/div[2]/button').click()
sleep(1)

# Enter number
number_input = browser.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]/input')
number_input.send_keys(number)
sleep(1)

# Enter password
pass_input = browser.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[3]/input')
pass_input.click()
pass_input.clear()
pass_input.send_keys(password)

# Login
browser.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[3]/div[1]/button').click()

sleep(5)

while True:
  text_area = browser.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/textarea')
  sleep(5)
  text_area.click()
  text_area.send_keys(text_msg)
  # enviar
  text_area.send_keys(Keys.RETURN)
