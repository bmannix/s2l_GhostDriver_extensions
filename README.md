s2l\_GhostDriver\_extensions
==========================

Some convenience methods for interfacing GhostDriver with RobotFramework's Selenium2Library 

ghost\_extenstions.py
--------------------

Contains the following keywords:

* Open Popup     - Clicks a webelement that will cause a popup to open, and switches the window to the popup.
* Close Popup    - Closes a popup that was opened with Open Popup, and switches back to the main window.
* Prep Alert     - Overrides window.alert to simple store the alert message rather than actually display an alert.
* Get Last Alert - Gets the message text of the last alert that was caused in the session.

Testing.html
------------

A robot framework test suite for these keywords with examples.  Selenium2Library is required.
