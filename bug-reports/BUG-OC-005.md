BUG-OC-005

Title: 522 connection timeout - Demo Site is unresponsive

Environment: Chrome Browser version 148; Android version 16

Severity: Critical

Priority: Critical

Preconditions: N/A

Steps to Reproduce:
1.navigate to any portion of OpenCart (https://demo.opencart.com/en-gb/catalog/cameras)

2. observe the spinner; page fails to render

3. after several seconds, encounter a 522 Connection Time Out error

Expected Result: user should be able to navigate the site normally

Actual Result: the site has become unresponsive; cannot navigate

Status: NEW

Notes:  
Screenshots of error acquired at 6/6/26 @0305, 0306 UTC. 
Errors appears consistent; not intermittent.
Error replicates in other environments (IE: Chrome mobile browser hosted on Google Pixel 8); replication indicates the error is server-level

<img width="1811" height="791" alt="Capture3" src="https://github.com/user-attachments/assets/889edcc6-dc60-415f-9c7c-0b45cdd67b8c" />
<img width="713" height="879" alt="Capture4" src="https://github.com/user-attachments/assets/bbdff544-0597-4cf9-905c-912f60d2d891" />


