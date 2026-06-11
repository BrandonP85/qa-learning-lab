BUG-TI-005

Title: "Internal server error" on 'Forgot Password'

Environment: Chrome Browser version 148

Severity: medium

Priority: low

Preconditions: must have a valid email. Example: "example@gmail.com"

Steps to Reproduce: 

1.navigate to The Internet (https://the-internet.herokuapp.com/)

2. from the Home page, navigate to 'Forgot Password'

3. input your email; press 'retrieve password'

4. see an "Internal Server Error" on the next page


Expected Result: the 'retrieve password' option should allow for a password reset

Actual Result: the option populates the error instead

Status: NEW

Notes:
Screenshot of the page with console error: "500 (Internal Server Error)"

<img width="1891" height="548" alt="Capture123" src="https://github.com/user-attachments/assets/defa99db-2683-4963-b380-1aa929b91c30" />

