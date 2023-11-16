from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from database import SessionLocal
from selenium_config import configure_web_driver
from schemas import Discount

db = SessionLocal()


def scrape_discount_information_from_jumia():
    # url = f"https://www.jumia.com.ng/mlp-black-friday/"
    url = f"https://www.jumia.com.ng/"
    driver = configure_web_driver(url)
    item_list = driver.find_elements(by=By.CLASS_NAME, value="core")
    for item in item_list:
        try:
            # Find the article element
            id = item.get_attribute("data-id")
            name = item.find_element(By.CLASS_NAME, "name")
            discount_price = item.find_element(By.CLASS_NAME, "prc")
            normal_price = item.find_element(By.CLASS_NAME, "prc").get_attribute("data-oprc")
            discount_percentage = item.find_element(By.CLASS_NAME, "bdg._dsct")
            link = item.get_attribute("href")
            company_name = item.get_attribute("data-brand")
            product_image = item.find_element(By.TAG_NAME, "img").get_attribute("data-src")
            print(id)
            product_discount = Discount(
                name_of_company=company_name,
                discount_product_name=name.text,
                discount_price=discount_price.text,
                normal_price=normal_price,
                discount_percentage=discount_percentage.text,
                discount_product_url=link,
                discount_product_image_url=product_image,
            )
            db.add(product_discount)
            db.commit()
        except NoSuchElementException:
            print("No discount")


if __name__ == "__main__":
    scrape_discount_information_from_jumia()
