<img width="1602" height="999" alt="API_Test" src="https://github.com/user-attachments/assets/819bc6a6-5d1c-433c-92c2-750b2b2a8f41" />
<img width="1602" height="999" alt="API_Test" src="https://github.com/user-attachments/assets/668e1796-8517-4e1e-894a-b327dd6243d6" />
# Restful-Booker API Testing Practice

Documenting my journey learning API testing with Postman and the Restful-Booker demo API.

## Milestone: Successful Authentication
**Date:** July 23, 2026

**Achievement:**
- Successfully sent a POST request to the `/auth` endpoint
- Used correct credentials: `admin` / `password123`
- Received a valid authentication token

**Key Lesson Learned:**
Postman sometimes caches request state. Always start with a fresh request tab when troubleshooting body/content-type issues.

**Request Details:**
- Method: `POST`
- URL: `https://restful-booker.herokuapp.com/auth`
- Body (raw JSON):
  ```json
  {
    "username": "admin",
    "password": "password123"
  }


