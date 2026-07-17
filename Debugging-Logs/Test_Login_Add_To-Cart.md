Automation Debug Log: Saucedemo login; add item to cart

Date: 7/17/26

Tester: Brandon P

Target: [https://demo.opencart.com/en-gb?route=account/login](https://www.saucedemo.com/inventory.html)

Environment: Chrome 418, Windows; Pythonn 3.12, Playwright

Issue Log:

Error observed: during automation testing of the login function of https://demo.opencart.com/en-gb?route=account/login, noted the process was timing out; 
the timeout was occuring when trying to click the login button

Hypothesis: the "Click" command in Python is targetting the wrong element

Fix Attempted:

Inspected the login button element using DevTools

corrected the automation testing code to allow for the form to become fully interactive by inserting "page.click("#login-button")". The standard options ('input', 'class' etc) 
were failing to properly point to the area.

re-tested; test successful

Result: the root cause was due to the design of the element in the HTML
Note: going forward, will utilize the ID ("#") to target elements in the most direct manner. This should prevent such an occurrence in the future.

![Uploading 10756.jpg…]()


