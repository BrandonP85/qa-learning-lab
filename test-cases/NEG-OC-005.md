NEG-OC-005

Title: Register new account without a correct email address

Preconditions: must have a valid email address

Steps to Perform:

1: navigate to https://demo.opencart.com/

2: click the "My account" drop down in the top-right

3: choose "register" in the drop down menu

4: fill in the necessary credentials - First Name, Last Name; input an invalid email address (example: 123456@987)

5: choose whether or not you want to subscribe by clicking the bottom-left switcher

6: accept the privacy policy on the bottom right

7: click "continue"

8: receive an error: Email address does not appear to be valid!

Expected Results: should not be able to create an account without a proper email address

Actual Results: cannot successfully create the account without a proper email address

Status: PASS

Notes: updating the UI to include a flag on a bad email address before the continue button is pressed would prevent this error for users.
