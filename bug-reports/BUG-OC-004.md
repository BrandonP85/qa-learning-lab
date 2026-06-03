BUG-OC-004

Title: 'Desktops' display (13), but specific groups don't match

Environment: Chrome Browser version 148

Severity: Low

Priority: Low

Preconditions: must be registered and logged in 

Steps to Reproduce: 
1.navigate to https://demo.opencart.com/en-gb?route=common/home 
2. click "My Account" in the top-right 
3. choose "login" from the drop-down 
4. login with your email address and password
5. from the Home page, click on 'Tablets'
6. on the next page, click 'Desktops' on the left; note that it shows (13) items
7. once clicked, notice the options, 'Mac' and "PC', only have (1) between them

Expected Result: the interface should indicate a matching value (13 should display 1)

Actual Result: the incorrect number displays instead

Status: NEW

Notes: screenshot of the issue
<img width="451" height="666" alt="Capture2" src="https://github.com/user-attachments/assets/d0c06ccc-0684-4b59-b86f-0835c1dd7a45" />
