import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('chromedriver')

driver = webdriver.Chrome(service=s)
driver.get("https://www.jetpunk.com/user-quizzes/176412/fast-math-randomized-multiplication-in-30-seconds")
driver.maximize_window()


outcomes = []
index = 0

body = driver.find_element(By.ID, "grid")
sums = body.find_elements(By.CLASS_NAME, "gx2 div.h")
start = driver.find_element(By.CLASS_NAME, "green")
start.click()

inputfield = driver.find_element(By.ID, "txt-answer-box")

print(f"Length of sums before: {len(sums)}")
while index < len(sums):
    if sums[index].text == "":
        sums.remove(sums[index])
    index += 1
print(f"Length of sums after: {len(sums)}")

for sum in sums:
    split_sum = sum.text.split()
    split_sum.remove("x")
    print(f"Split sum: {split_sum}")
    outcome = int(split_sum[0]) * int(split_sum[1])
    print(f"Outcome: {outcome}")
    outcomes.append(outcome)
    for answer in outcomes:
        outcomes.remove(outcomes[0])
        print(f"Answer: {answer}")
        inputfield.send_keys(answer)