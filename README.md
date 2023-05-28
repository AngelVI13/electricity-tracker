# Usage

1. Install libraries
`python -m pip install -r requirements.txt`

2. Install webdriver

[Selenium Webdriver Docs](https://selenium-python.readthedocs.io/installation.html#drivers)

Ibex loads its data dynamically so you can't just make a get request to the website and 
scrape the data because it won't be in the html directly. Instead you have to use a webdriver 
to evaluate the html+js and that will calculate the displayed values.
