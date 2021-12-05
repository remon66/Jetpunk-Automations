from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.get("https://www.jetpunk.com/user-quizzes/91108/multiplication-table-quiz")
driver.maximize_window()


def fillIn():
    start = driver.find_element(By.CLASS_NAME, "green")
    start.click()

    inputField = driver.find_element(By.ID, "txt-answer-box")

    x = 1
    y = 1
    answers = []
    index = 1

    while y <= 12:
        answers.append(x * y)
        y+=1

    for answer in answers:
        inputField.send_keys(answer)


fillIn()
