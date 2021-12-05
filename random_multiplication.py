from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.get("https://www.jetpunk.com/user-quizzes/176412/fast-math-randomized-multiplication-in-30-seconds")
driver.maximize_window()


outcoms = []

sums = driver.find_elements(By.CLASS_NAME, "gx2 .h")

for sum in sums:
    if sum == "":
        print("empty sum")
    else:
        split_sum = sum.text.split()
        print(split_sum)
