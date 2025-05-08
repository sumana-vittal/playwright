from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False )
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Index.html')

    #css
    page.wait_for_selector('#email').type('test@gmail.com')
    page.wait_for_selector('#enterimg').click()
    page.wait_for_timeout(3000)
