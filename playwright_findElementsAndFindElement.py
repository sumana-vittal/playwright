from pydoc import pager

from playwright.sync_api import sync_playwright

with sync_playwright() as pw:

    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demo.nopcommerce.com/register")

    #find_element
    # page.locator("[id='small-searchterms']").fill('abc')
    page.fill("[id='small-searchterms']", 'abc')
    page.wait_for_timeout(5000)

    #find_elements
    all_texts = page.locator("//div[@class='footer']//a").all()
    for txt in all_texts:
        print(txt.text_content())

