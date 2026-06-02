NEG-OC-007

Title: Register new account without filling out required info

Preconditions: must have a valid email address

Steps to Perform:

1: navigate to https://demo.opencart.com/

2: click the "My account" drop down in the top-right

3: choose "register" in the drop down menu

4: fill in the necessary credentials - leave 'First Name' blank; fill out Last Name; input an valid email address

5: choose whether or not you want to subscribe by clicking the bottom-left switcher

6: accept the privacy policy on the bottom right

7: click "continue"

8: receive an error: First Name must be between 1 and 32 characters!

Expected Results: should not be able to create an account without a first name

Actual Results: cannot successfully create the account without a first name

Status: FAIL

Notes: updating the UI to include a flag on an empty required field before the continue button is pressed would prevent this error for users.
