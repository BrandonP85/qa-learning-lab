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


