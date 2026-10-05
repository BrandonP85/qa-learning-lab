<img width="1911" height="1041" alt="booking1" src="https://github.com/user-attachments/assets/2fb0dab1-2a03-4490-81ac-15a3e44bbee9" />
<img width="1799" height="950" alt="booking2" src="https://github.com/user-attachments/assets/f9e93747-3972-4b27-9a8f-59485e411899" />
<img width="1774" height="976" alt="booking3" src="https://github.com/user-attachments/assets/2dd9fa76-f106-409e-87fb-a1c1d9c2d1bd" />

# Restful-Booker API Testing Practice
Documenting my journey learning API testing with Postman and the Restful-Booker demo API.

Milestone: Successful Authentication
Date: 4 Oct 2026

Achievement:

Successfully sent a POST request to the /auth endpoint
Successfully pulled a Booking List from Restful-Booker with GET
Successfully debugged a Server Error 500 when attempting to POST a new booking
Successfully completed POST request

Lesson learned: Postman is sensitive to the spacing of elements, like colons. Make sure proper spacing is used.

Request Details:

Method: POST
URL: https://restful-booker.herokuapp.com/auth
Body (raw JSON):

    {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": true,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
    }
