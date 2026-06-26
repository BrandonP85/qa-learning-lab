C:\Users\Fathe\Desktop\playwright_tests> python Test_login.py
Traceback (most recent call last):
  File "C:\Users\Fathe\Desktop\playwright_tests\Test_login.py", line 20, in <module>
    test_login()
  File "C:\Users\Fathe\Desktop\playwright_tests\Test_login.py", line 9, in test_login
    page.fill("input[name='email']", "Thisemail@gmail.com")
  File "D:\Python312\Lib\site-packages\playwright\sync_api\_generated.py", line 10998, in fill
    self._sync(
  File "D:\Python312\Lib\site-packages\playwright\_impl\_sync_base.py", line 115, in _sync
    return task.result()
           ^^^^^^^^^^^^^
  File "D:\Python312\Lib\site-packages\playwright\_impl\_page.py", line 917, in fill
    return await self._main_frame.fill(**locals_to_params(locals()))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python312\Lib\site-packages\playwright\_impl\_frame.py", line 610, in fill
    await self._fill(**locals_to_params(locals()))
  File "D:\Python312\Lib\site-packages\playwright\_impl\_frame.py", line 622, in _fill
    await self._channel.send("fill", self._timeout, locals_to_params(locals()))
  File "D:\Python312\Lib\site-packages\playwright\_impl\_connection.py", line 69, in send
    return await self._connection.wrap_api_call(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Python312\Lib\site-packages\playwright\_impl\_connection.py", line 559, in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
playwright._impl._errors.TimeoutError: Page.fill: Timeout 30000ms exceeded.
Call log:
  - waiting for locator("input[name='email']")
    - waiting for navigation to finish...
    - navigated to "https://demo.opencart.com/en-gb?route=account/login"
