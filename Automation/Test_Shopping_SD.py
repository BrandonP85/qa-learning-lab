import playwright.sync_api
def Test_Shopping():
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
        page.wait_for_timeout(2000)
        page.click("button[name='add-to-cart-sauce-labs-bike-light']") # Click the "Add to cart" button for the specific product (Sauce Labs Bike Light)

        assert "/inventory.html" in page.url, f"Add to cart failed. Current URL: {page.url}" # Assert that the current URL still contains "/inventory.html" to verify that the user is still on the inventory page after adding the item to the cart
        print("Add to cart successful") # Log message indicating that the item was successfully added to the cart

        page.goto("https://www.saucedemo.com/cart.html") # Navigate to the cart page
        page.wait_for_timeout(2000)
        page.click('#remove-sauce-labs-bike-light') # Click the "Remove" button for the specific product (Sauce Labs Bike Light)

        assert "/cart.html" in page.url, f"Remove from cart failed. Current URL: {page.url}" # Assert that the current URL still contains "/cart.html" to verify that the user is still on the cart page after removing the item from the cart
        print("Remove from cart successful") # Log message indicating that the item was successfully removed from the cart

        page.goto("https://www.saucedemo.com/inventory.html") # Navigate back to the inventory page
        page.wait_for_timeout(2000)
        page.click("button[name='add-to-cart-sauce-labs-backpack']") # Click the "Add to cart" button for the specific product (Sauce Labs Backpack)
        print("Add to cart successful") # Log message indicating that the item was successfully added to the cart

        cart_badge = page.locator(".shopping_cart_badge") # Locate the cart badge element that displays the number of items in the cart
        assert cart_badge.is_visible(), "Cart badge not visible after adding backpack" # Assert that the cart badge is visible after adding the backpack to the cart
        assert cart_badge.inner_text() == "1", f"Expected 1 item in cart, got: {cart_badge.inner_text()}" # Assert that the cart badge displays the correct number of items
        print("Cart verified — 1 item in cart") # Log message indicating that the cart has been verified and contains 1 item

        browser.close()

Test_Shopping()
