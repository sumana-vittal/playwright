from playwright.sync_api import sync_playwright

text_alert = []
def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.accept()


with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()

    # page.goto("https://demo.automationtesting.in/Register.html")
    #
    # page.check("input[value='FeMale']")
    #
    # page.check("[id='checkbox1']")

    # page.close()

    page.goto("https://demo.automationtesting.in/Alerts.html")

    #by default playwright selects ok
    page.wait_for_selector("//a[@href='#CancelTab']").click()

    # page.on("dialog", lambda dialog: print(dialog.message))
    page.on("dialog", handle_dialog)
    page.wait_for_selector("//div[@id='CancelTab']/button").click()

    page.wait_for_timeout(3000)
    print(text_alert[0])
