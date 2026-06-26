Automation Debug Log: Opencart Login

Date: 6/26/26

Tester: Brandon P

Target: https://demo.opencart.com/en-gb?route=account/login

Environment: Chrome 418, Windows; Pythonn 3.12, Playwright

**Issue Log:**

**Error observed:** during automation testing of the login function of https://demo.opencart.com/en-gb?route=account/login, noted the process was timing out
the timeout was occurring when the automation was trying to find "input[name='email']"

**Hypothesis:** the email field selector is named differently in the OpenCart HTML

**Fix Attempted:** 
> determined that the input written correctly in the HTML

> corrected the automation testing code to allow for the form to become fully interactive by inserting "page.wait_for_selector("input[name='email']")"

> re-tested; error still occured: "TimeoutError: Page.wait_for_selector: Timeout 30000ms exceeded."

> added in "page.screenshot(path="debug_screenshot.png")" to screenshot the problem area

> re-tested; determined the core issue is Cloudflare blocking bot activity. The automation is never able to touch the site.


**Result:** the root cause was due to a function of the target testing site Working as Designed

**What was learned:** Cloudflare bot protection is a legitimate constraint; Demo environments with active bot mitigation are not suitable Playwright targets without Stealth tools. Future targets will be verified for bot protection to prevent an outcome like this in the future; the failure was environmental, not code-level. 

**Command Prompt Test Result Code**
C:\Users\Fathe\Desktop\playwright_tests> python Test_login.py
Traceback (most recent call last):
  File "C:\Users\Fathe\Desktop\playwright_tests\Test_login.py", line 21, in <module>
    test_login()
  File "C:\Users\Fathe\Desktop\playwright_tests\Test_login.py", line 8, in test_login
    page.wait_for_selector("input[name='email']")
  File "D:\Python312\Lib\site-packages\playwright\sync_api\_generated.py", line 8770, in wait_for_selector
    self._sync(
  File "D:\Python312\Lib\site-packages\playwright\_impl\_sync_base.py", line 115, in _sync
    return task.result()
           ^^^^^^^^^^^^^
  File "D:\Python312\Lib\site-packages\playwright\_impl\_page.py", line 424, in wait_for_selector
    return await self._main_frame.wait_for_selector(**locals_to_params(locals()))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python312\Lib\site-packages\playwright\_impl\_frame.py", line 372, in wait_for_selector
    await self._channel.send(
  File "D:\Python312\Lib\site-packages\playwright\_impl\_connection.py", line 69, in send
    return await self._connection.wrap_api_call(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python312\Lib\site-packages\playwright\_impl\_connection.py", line 559, in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
playwright._impl._errors.TimeoutError: Page.wait_for_selector: Timeout 30000ms exceeded.
Call log:
  - waiting for locator("input[name='email']") to be visible


C:\Users\Fathe\Desktop\playwright_tests> python Test_login.py
Traceback (most recent call last):
  File "C:\Users\Fathe\Desktop\playwright_tests\Test_login.py", line 22, in <module>
    test_login()
  File "C:\Users\Fathe\Desktop\playwright_tests\Test_login.py", line 9, in test_login
    page.wait_for_selector("input[name='email']")
  File "D:\Python312\Lib\site-packages\playwright\sync_api\_generated.py", line 8770, in wait_for_selector
    self._sync(
  File "D:\Python312\Lib\site-packages\playwright\_impl\_sync_base.py", line 115, in _sync
    return task.result()
           ^^^^^^^^^^^^^
  File "D:\Python312\Lib\site-packages\playwright\_impl\_page.py", line 424, in wait_for_selector
    return await self._main_frame.wait_for_selector(**locals_to_params(locals()))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python312\Lib\site-packages\playwright\_impl\_frame.py", line 372, in wait_for_selector
    await self._channel.send(
  File "D:\Python312\Lib\site-packages\playwright\_impl\_connection.py", line 69, in send
    return await self._connection.wrap_api_call(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python312\Lib\site-packages\playwright\_impl\_connection.py", line 559, in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None

playwright._impl._errors.TimeoutError: Page.wait_for_selector: Timeout 30000ms exceeded.
Call log:
  - waiting for locator("input[name='email']") to be visible

**Screenshots** of the Automation test script and the Debug screenshot result:
<img width="1280" height="720" alt="debug_screenshot" src="https://github.com/user-attachments/assets/8b4a5155-78a4-4332-aad0-af8d56c752ab" />
<img width="1116" height="632" alt="CodeSS1" src="https://github.com/user-attachments/assets/4b67e201-61f8-4acc-8087-25a08d87f41e" />
<img width="996" height="576" alt="CodeSS2" src="https://github.com/user-attachments/assets/f15516f2-8c52-492a-bc4f-d14f20ebb99e" />


