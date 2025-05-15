from playwright.sync_api import sync_playwright
from sqlalchemy.sql.base import elements

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demo.nopcommerce.com/register")

    #application commands
    page.wait_for_load_state('load')
    print(page.title())
    print(page.url)
    print(page.content())

    #Conditional commands
    element = page.locator("[id='gender-male']")
    print(element.is_checked())
    print(element.is_disabled())
    print(element.is_enabled())
    print(element.is_hidden())
    print(element.is_visible())

    #browser commands
    # page.close()#driver.close()
    # browser.close()#driver.quit()

    #navigational commands
    page.goto("https://www.amazon.com")
    page.go_back()
    page.go_forward()
    page.reload() # for refresh




    browser.close()