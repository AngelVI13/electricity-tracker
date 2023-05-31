import requests
from datetime import datetime
from bs4 import BeautifulSoup

LIMIT = 0.0

DATA_URL = "https://ibex.bg/dev/ID24/data_bg.php"


def main():
    user_agent = {'User-agent': 'Mozilla/5.0'}
    resp = requests.get(DATA_URL, headers=user_agent)

    soup = BeautifulSoup(resp.text, "html.parser")
    div = soup.find(attrs={"class": "idm-table"})

    elems = div.find_all(attrs={"class": "column-avg"})

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


if __name__ == "__main__":
    main()
