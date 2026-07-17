import playwright.sync_api
def test_Add_Light():
    with playwright.sync_api.sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/") # Navigate to the login page
        page.wait_for_timeout(2000)  # Wait for 2 seconds to ensure the page is fully loaded
        page.screenshot(path="debug_screenshot2.png") # Take a screenshot for debugging purposes
        print("screenshot taken") # Log message indicating that the screenshot has been taken

    

        page.fill("input[name='user-name']", "standard_user") # Fill in the username field with the provided username
        page.fill("input[name='password']", "secret_sauce") # Fill in the password field with the provided password

        page.click("#login-button") # Click the login button

        assert "/inventory.html" in page.url, f"Login failed. Current URL: {page.url}" # Assert that the current URL contains "/inventory.html" to verify successful login
        print("Login successful") # Log message indicating that the login was successful

        page.goto("https://www.saucedemo.com/inventory.html") # Navigate to the inventory page
        page.click("button[name='add-to-cart-sauce-labs-bike-light']") # Click the "Add to cart" button for the specific product (Sauce Labs Bike Light)

        assert "/inventory.html" in page.url, f"Add to cart failed. Current URL: {page.url}" # Assert that the current URL still contains "/inventory.html" to verify that the user is still on the inventory page after adding the item to the cart
        print("Add to cart successful") # Log message indicating that the item was successfully added to the cart

        browser.close()

test_Add_Light()
