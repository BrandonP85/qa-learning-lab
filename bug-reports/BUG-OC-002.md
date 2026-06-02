BUG-OC-002

Title: inadequate password entry on registration page returns inline prompt for password length; no requirements shown

Environment: Chrome Browser version 148

Severity: Low

Priority: Low

Preconditions: N/A

Steps to Reproduce:
1.navigate to https://demo.opencart.com/en-gb?route=common/home
2. click "My Account" in the top-right
3. choose "register" from the drop-down
4. on the register page, enter the fields (name, email address, etc)
5. enter a short password (1-3 characters) or a very long password (over 20 characters)
6. accept the Privacy Policy on the bottom/right
7. Press "continue"
8. receive an error: "Password must be between 4 and 20 characters!"

Expected Result: password requirements should be displayed for the user

Actual Result: instead of being displayed, they are presented as an inline error

Status: NEW

Notes: Screenshot: inline password prompt response
<img width="1441" height="929" alt="Capture2" src="https://github.com/user-attachments/assets/85300b7d-2696-4af3-8786-112bc8adec7e" />
