from playwright.sync_api import sync_playwright

with sync_playwright() as pw :
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demo.automationtesting.in/Register.html")


    #selenium method
    # skill_dropdown = page.query_selector("[id='Skills']")
    # skill_dropdown.select_option(label='Android')
    # page.wait_for_timeout(3000)

    #playwright method
    page.select_option("[id='Skills']",label='Android')
    page.wait_for_timeout(3000)
