from bs4 import BeautifulSoup
import requests
from playwright.sync_api import sync_playwright


def web_scrapper_mvp(url, keyword):
    with sync_playwright() as p:

        # open the browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # navigate to the url
        page.goto(url)

        # wait for it to load
        page.wait_for_load_state('networkidle')

        # scrape the content
        html_content = page.content()

        # close the browser
        browser.close()

        # use BeautifulSoup to parse it
        soup = BeautifulSoup(html_content, 'html.parser')

        page_text = soup.get_text().lower()

        # DIRECT EQUIV CHACKER
        # for word in page_text.split():

        #     if word == keyword.lower():

        #         print("yay time to apply :)))))")

        # print("bruh fuck this company those little ass shitholes")

        # KEYWORD PRESENT CHECKER
        return keyword.lower() in page_text


# enter the url adn keyword
url_heidi = 'https://jobs.ashbyhq.com/heidihealth.com.au?locationId=ceba48bb-5187-4893-ad99-6bac90954697'
url_euc = "https://www.eucalyptus.health/careers#open-roles"


keyword = 'sales'

# test the function
if web_scrapper_mvp(url_heidi, keyword):
    print("haha i can apply now")

else:
    print("fuck this company")
