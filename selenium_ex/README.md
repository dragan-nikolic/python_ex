# Selenium Examples

## Installation

`$ pip install selenium`

### Install webdrivers

* [chromedriver](https://chromedriver.chromium.org/downloads)

#### Mac

`$ brew cask install chromedriver`
`$ brew install geckodriver`

Note: If Mac refuses to start a driver because it's not verified, just open the same driver
manually using Finder.

## Usage

`from selenium import webdriver`
`from selenium.webdriver.common.keys import Keys`

`driver = webdriver.Chrome('./chromedriver')`
`driver.get("https://www.python.org")`

## References

* [Browser Stack Tutorial](https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test)