from playwright.sync_api import sync_playwright
def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")
        page.screenshot(path="debug_screenshot.png")
        page.wait_for_selector("input[name='username']")

        page.fill("input[name='username']", "tomsmith")
        page.fill("input[name='password']", "SuperSecretPassword!")

        page.click("button[type='Submit']")

        assert "/secure" in page.url, f"Login failed. Current URL: {page.url}"

        print("Login test passed.")

        browser.close()

test_login()


def test_login_invalid_credentials():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://the-internet.herokuapp.com/login")
        page.screenshot(path="debug_screenshot.png")
        page.wait_for_selector("input[name='username']")

        page.fill("input[name='username']", "nwrongdude")
        page.fill("input[name='password']", "WrongSecretPassword!")

        page.click("button[type='Submit']")

        error = page.locator(".alert-danger") 
        assert error.is_visible, "expected error message not displayed"

        print("Invalid login test passed.")

        browser.close()

test_login_invalid_credentials()
