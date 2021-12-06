from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('chromedriver')

driver = webdriver.Chrome(service=s)
driver.get("https://www.jetpunk.com/quizzes/fast-typing-to-hundred-quiz")
driver.maximize_window()

start = driver.find_element(By.CLASS_NAME, "green")
start.click()

inputfield = driver.find_element(By.ID, "txt-answer-box")

count = 1

while count <= 100:
    inputfield.send_keys(count)
    count+=1
