NEG-TC-006

Title: Register new account with an already registered email

Preconditions: must have a valid email address; must have already registered

Steps to Perform:

1: navigate to https://demo.opencart.com/

2: click the "My account" drop down in the top-right

3: choose "register" in the drop down menu

4: fill in the necessary credentials - First Name, Last Name; input a email address that is already registered

5: choose whether or not you want to subscribe by clicking the bottom-left switcher

6: accept the privacy policy on the bottom right

7: click "continue"

8: receive an error: E-Mail Address is already registered!

Expected Results: should not be able to create an account with an email address hat is already registered

Actual Results: cannot successfully create the account without an email address already registered

Status: FAIL

Notes: updating the UI to include a flag on an already registered email address before the continue button is pressed would prevent this error for users.
