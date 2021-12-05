from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.get("https://www.jetpunk.com/user-quizzes/176412/fast-math-randomized-multiplication-in-30-seconds")
driver.maximize_window()


outcoms = []

sums = driver.find_elements(By.CLASS_NAME, "gx2 .h")
start = driver.find_element(By.CLASS_NAME, "green")
start.click()

inputfield = driver.find_element(By.ID, "txt-answer-box")

for sum in sums:
    if len(sums) == 0:
        print("empty")
    else:
        split_sum = sum.text.split()
        if len(split_sum) == 0:
            continue
        split_sum.remove("x")
        inputfield.send_keys(int(split_sum[0]) * int(split_sum[1]))
