from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    #css
    # page.wait_for_selector("input[name='username']").type('Admin')
    # page.wait_for_selector("input[type='password']").type("admin123")
    # page.wait_for_selector("button[type='submit']").click()

    #xpath
    page.wait_for_selector("//input[@name='username']").type("Admin")
    page.wait_for_selector("//input[@placeholder='Password']").type("admin123")
    # page.wait_for_selector("//button[@type='submit']").click()


    #xpath functions - text(), contains, starts-with, ends-with
    # page.wait_for_selector("//p[text()='Forgot your password? ']").click()
    # page.wait_for_selector("//p[text()[contains(.,'Forgot')]]").click()
    page.wait_for_selector("//p[contains(@class,'orangehrm-login-forgot-header')]")

    page.wait_for_timeout(3000)