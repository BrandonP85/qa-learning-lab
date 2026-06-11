BUG-TI-003

Title: Broken page load on "Slow Resources"

Environment: Chrome Browser version 148

Severity: low

Priority: low

Preconditions: N/A

Steps to Reproduce: 

1.navigate to The Internet (https://the-internet.herokuapp.com/)

2. from the Home page, navigate to 'Slow Resources'; click it

3. the page advises that it should take 30 seconds to load a rogue element 

4. monitor the page; it does not load anything after the time frame. Tested a 120 second wait to validate


Expected Result: the GET request should load, per the instructions

Actual Result: it does not load anything, even after the 30 seconds

Status: NEW

Notes:
Screenshot of the page with console error: "503 (Service Unavailable)"

<img width="1909" height="556" alt="Capture11" src="https://github.com/user-attachments/assets/780ecfdb-89e9-4648-8cff-12fa962c73cf" />
