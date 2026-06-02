NEG-OC-009

Title: Attempt login with unregistered email

Preconditions: must not use a registered email

Steps to Perform:

1: navigate to https://demo.opencart.com/

2: click the "My account" drop down in the top-right

3: choose "login" in the drop down menu

4: input incorrect email address (Brandon@noemail.com)

5: input correct password

6: receive an error: No match for E-Mail and/or Password.

Expected Results: should not be able to login with an unregistered email

Actual Results: cannot login with an unregistered email

Status: FAIL

Notes: Specific error recomended; "invalid email" or similar. Understably, I realize this error may exist to prevent enumeration attacks.
