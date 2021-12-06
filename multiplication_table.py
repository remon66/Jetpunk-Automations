from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("chromedriver")

driver = webdriver.Chrome(service=s)
driver.get("https://www.jetpunk.com/user-quizzes/91108/multiplication-table-quiz")
driver.maximize_window()


def fillin():
    start = driver.find_element(By.CLASS_NAME, "green")
    start.click()

    inputfield = driver.find_element(By.ID, "txt-answer-box")

    x = 1
    y = 1
    answers = []

    while x <= 12:
        while y <= 12:
            answers.append(x * y)
            y+=1
        x+=1
        y = 1

    for answer in answers:
        inputfield.send_keys(answer)


fillin()
