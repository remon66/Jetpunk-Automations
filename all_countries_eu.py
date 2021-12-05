from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.jetpunk.com/quizzes/landen-van-de-wereld")
driver.maximize_window()
fast = True


def fillIn():
    start = driver.find_element(By.CLASS_NAME, "green")
    start.click()

    countries = "Albanië Andorra Belarus België Bosnië Bulgarije Denemarken Duitsland Estland Finland Frankrijk Griekenland Hongarije Ierland IJsland Italië Kosovo Kroatië Letland Liechtenstein Litouwen Luxemburg Malta Moldavië Monaco Montenegro Nederland Noord-Macedonië Noorwegen Oekraïne Oostenrijk Polen Portugal Roemenië Rusland SanMarino Servië Slovenië Slowakije Spanje Tsjechië Vaticaan VerenigdKoninkrijk Zweden Zwitserland Afghanistan Armenië Azerbeidzjan Bahrein Bangladesh Bhutan Brunei Cambodja China Cyprus Filipijnen Georgië India Indonesië Irak Iran Israël Japan Jemen Jordanië Kazachstan Kirgizië Koeweit Laos Libanon Maldiven Maleisië Mongolië Myanmar Nepal Noord-Korea Oezbekistan Oman Oost-Timor Pakistan Qatar Saoedi-Arabië Singapore SriLanka Syrië Tadzjikistan Taiwan Thailand Turkije Turkmenistan VerenigdeArabischeEmiraten Vietnam Zuid-Korea Algerije Angola Benin Burundi Botswana Burkina Faso Centraal-AfrikaanseRepubliek Comoren Congo Djibouti Egypte Equatoriaal-Guinea Eritrea Eswatini Ethiopië Gabon Gambia Ghana Guinee Guinee-Bissau Ivoorkust Kaapverdië Kameroen Kenia Lesotho Liberia Libië Madagaskar Malawi Mali Marokko Mauritanië Mauritius Mozambique Namibië Niger Nigeria Oeganda Rwanda SaoTomé Senegal Seychellen SierraLeone Soedan Somalië Tanzania Togo Tsjaad Tunesië Zambia Zimbabwe Zuid-Afrika Zuid-Soedan Antigua Bahamas Barbados Belize Canada CostaRica Cuba Dominica DominicaanseRepubliek ElSalvador Grenada Guatemala Haïti Honduras Jamaica Mexico Nicaragua Panama SaintLucia SaintKitts SaintVincent Trinidad VerenigdeStaten Argentinië Bolivia Brazilië Chili Colombia Ecuador Guyana Paraguay Peru Suriname Uruguay Venezuela Australië Fiji Kiribati Marshalleilanden Micronesia Nauru Nieuw-Zeeland Palau Papoea-Nieuw-Guinea Samoa Salomonseilanden Tonga Tuvalu Vanuatu"
    inputField = driver.find_element(By.ID, "txt-answer-box")

    if fast:
        x = countries.split()
        for country in x:
            inputField.send_keys(country)
    else:
        for country in countries:
            inputField.send_keys(country)


fillIn()
