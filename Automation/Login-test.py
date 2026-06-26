from playwright.sync_api import sync_playwright
def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demo.opencart.com/en-gb?route=account/login")
        page.screenshot(path="debug_screenshot.png")
        page.wait_for_selector("input[name='email']")

        page.fill("input[name='email']", "Thisemail@gmail.com")
        page.fill("input[name='password']", "Winter@226!")

        page.click("input[value='Login']")

        assert "route=account/account" in page.url, f"Login failed. Current URL: {page.url}"

        print("Login test passed.")

        browser.close()

test_login()


def test_login_invalid_credentials():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demo.opencart.com/en-gb?route=account/login")
        page.screenshot(path="debug_screenshot.png")
        page.wait_for_selector("input[name='email']")

        page.fill("input[name='email']", "noemail@12345.com")
        page.fill("input[name='password']", "Winter21!")

        page.click("input[value='Login']")

        error = page.locator(".alert-danger") 
        assert error.is_visible, "expected error message not displayed"

        print("Invalid login test passed.")

        browser.close()

test_login_invalid_credentials()
