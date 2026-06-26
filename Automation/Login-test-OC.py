from playwright.sync_api import sync_playwright
def test_login():
    with sync_playwright() as p:
        
        # Launch Chromium in headed mode (visible browser window) for debugging visibility
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        #Navigate to the login page and wait until the username field is ready
        page.goto("https://demo.opencart.com/en-gb?route=account/login")
        page.screenshot(path="debug_screenshot.png")
        page.wait_for_selector("input[name='email']")
        
        # Fill in valid credentials for the happy path test
        page.fill("input[name='email']", "Thisemail@gmail.com")
        page.fill("input[name='password']", "Winter@226!")
        
        # Submit the login form
        page.click("input[value='Login']")
        
        # Assert successful login - valid login redirects to account/account
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
        
        # Fill in valid invalid credentials for the negative test
        page.fill("input[name='email']", "noemail@12345.com")
        page.fill("input[name='password']", "Winter21!")

        page.click("input[value='Login']")

        # Assert an error message due to the incorrect login
        error = page.locator(".alert-danger") 
        assert error.is_visible, "expected error message not displayed"

        print("Invalid login test passed.")

        browser.close()

test_login_invalid_credentials()
