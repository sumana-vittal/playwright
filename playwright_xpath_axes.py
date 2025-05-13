from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page()
    page.goto("https://selectorshub.com/xpath-practice-page/")

    #self
    # msg = page.locator("//a[text()='John.Smith']/self::a").text_content()
    # print(msg)

    #parent
    msg = page.locator("//a[text() = 'John.Smith']/parent:: *").inner_text()
    print(msg)

    #child - no direct child , so goto ancestor n try getting child
    msg = page.locator("//a[text()='John.Smith']/ancestor::tr/child::*").all_text_contents()
    print(msg)

    #ancestor
    msg = page.locator("//a[text()='John.Smith']/ancestor::tr").all_text_contents()
    print(msg)

    # # descendant
    msg = page.locator("//a[text()='John.Smith']/ancestor::tr/descendant::*").all_text_contents()
    print(msg)

    #following
    msg = page.locator("//a[text()='John.Smith']/following::tr").all_text_contents()
    print(msg)

    # follwing-sibling
    msg = page.locator("//a[text()='John.Smith']/ancestor::tr/following-sibling::tr").all_text_contents()
    print(msg)

    #preceding
    msg = page.locator("//a[text()='John.Smith']/ancestor::tr/preceding::tr").all_text_contents()
    print(msg)

    # preceding-sibling
    msg = page.locator("//a[text()='John.Smith']/ancestor::tr/preceding-sibling::tr").all_text_contents()
    print(msg)


