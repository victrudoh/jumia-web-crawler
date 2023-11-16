from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chromeService = Service("/Users/newowner/PycharmProjects/jumia-discount-crawler/selenium/chromedriver.exe")
headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Accept, X-Requested-With"
}


def configure_web_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")  ## This flag dialog/ information Dialog
    options.add_argument('start-maximized')  ## Start the brower in full desktop mode
    options.add_argument('disable-dev-shm-usage')  ## For linux based machines
    options.add_argument('no-sandbox')  ## disable sanbox
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  ## Removes automation warning from chrome
    options.add_argument('disable-blink-features=AutomationControlled')
    # Add headers as arguments
    for key, value in headers.items():
        options.add_argument(f"--{key}={value}")
    driver = webdriver.Chrome(options=options)
    driver.get(url=url)
    return driver
