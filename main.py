import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://ibex.bg/данни-за-пазара/пазарен-сегмент-в-рамките-на-деня/idm-prices-volumes-with-qh-2/"


def main():
    driver = webdriver.Firefox()
    driver.get(url)

    # NOTE: have to wait some time until all data in the table is populated
    # `WebDriverWait` is not sufficient
    time.sleep(5)  # seconds

    table = driver.find_element(By.CLASS_NAME, "idm-table")
    elems = table.find_elements(By.CLASS_NAME, "column-avg")

    if len(elems) != 24:
        raise Exception(
            f"expected 24 prices (one for every hour) but got {len(elems)} instead"
        )

    for e in elems:
        print(e.text)

    driver.close()


if __name__ == "__main__":
    main()
