from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    # default headless is True. Set it to false.
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com/")
    print("chrome launched..")
    print(page.title())
    browser.close()