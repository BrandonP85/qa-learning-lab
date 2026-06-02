BUG-OC-001

Title: empty field submission generates the same error as incorrect inputs

Environment: Chrome Browser version 148

Severeity: Medium

Priority: Low

preconditions: N/A

Steps to Reproduce:
1. navigate to https://demo.opencart.com/en-gb?route=common/home
2. click "My Account" in the top-right
3. choose "login" from the drop-down 
4. on the login page, leave either Email address, Password, or both blank
5. press "login"
6. receive an error: "No match for E-Mail Address and/or Password"

Expected Result: the system should flag the field as empty

Actual Result: the sytem instead throws the same alert as an incorrect input

Status: NEW

Notes: <img width="1829" height="864" alt="Capture" src="https://github.com/user-attachments/assets/d271fce5-8ed3-4250-8194-087b027a3227" />
