import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

URL = "https://ibex.bg/данни-за-пазара/пазарен-сегмент-в-рамките-на-деня/idm-prices-volumes-with-qh-2/"
LIMIT = 75.0


def main():
    # if you dont want the browser to open on every run, set "headless" option to the driver
    # options = Options()
    # options.add_argument("--headless")
    # driver = webdriver.Firefox(options=options)

    driver = webdriver.Firefox()
    driver.get(URL)

    # NOTE: have to wait some time until all data in the table is populated
    # `WebDriverWait` is not sufficient
    time.sleep(5)  # seconds

    table = driver.find_element(By.CLASS_NAME, "idm-table")
    elems = table.find_elements(By.CLASS_NAME, "column-avg")

    if len(elems) != 24:
        raise Exception(
            f"expected 24 prices (one for every hour) but got {len(elems)} instead"
        )

    # Get current date & time, we need the current hour to determine the current price
    now = datetime.now()
    hour = now.hour

    # elems is list of prices for each hour [0;23]
    price = elems[hour].text
    # prices are as 25,37 but float expects dot instead of comma
    price = price.replace(",", ".")

    try:
        price = float(price)
    except Exception:
        raise Exception(f"could not convert price to float: {price}")

    print(f"current price is {price}")

    if round(price, 2) >= round(LIMIT, 2):
        # PUT LOGIC HERE
        print("TODO")
    else:
        # PUT LOGIC HERE
        print("TODO")

    driver.close()


if __name__ == "__main__":
    main()
