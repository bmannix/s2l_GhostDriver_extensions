#!/usr/bin/env python

from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger

class UsageError(Exception):
    pass

def open_popup(locator):
    """ 
    Clicks a web element that will open a new popup window.
    """
    seleniumlib = BuiltIn().get_library_instance('Selenium2Library')
    browser = seleniumlib._current_browser()
    #saves the main window handle to an instance variablec
    seleniumlib.main_window = browser.current_window_handle
    logger.debug('Current window handle is: %s' % seleniumlib.main_window)
    before = set(browser.window_handles)
    seleniumlib.click_element(locator)
    after = set(browser.window_handles) 
    try:
        new_win = (after - before).pop()
    except KeyError:
        logger.warn("No new popup window was detected!")
        raise
    logger.debug('Switching to window: %s' % new_win)
    browser.switch_to_window(new_win)

def close_popup():
    """
    Closes a popup window that was opened with "Open Popup"
    """
    seleniumlib = BuiltIn().get_library_instance('Selenium2Library')
    if not hasattr(seleniumlib, 'main_window'):
        raise UsageError('Popups must be opened with the same Selenium2Library'
                         ' instance before they can be closed')
    #This overrides any modal creation (e.g. "are you sure?")
    seleniumlib.execute_javascript('window.onbeforeunload = function() {}')
    browser = seleniumlib._current_browser()
    logger.debug('Closing window: %s' % browser.current_window_handle)
    seleniumlib.close_window()
    logger.debug('Switching to window: %s' % seleniumlib.main_window)
    browser.switch_to_window(seleniumlib.main_window)

def prep_alert():
    """
    Overrides window.alert to simply store the alert message rather than
    display it.  This will become unnecessary once GhostDriver supports alerts
    natively.
    """
    seleniumlib = BuiltIn().get_library_instance('Selenium2Library')
    js = """
    window.alert = function(message) {
                lastAlert = message;
                }
    """
    logger.debug('Overriding window.alert to store the alert message')
    seleniumlib.execute_javascript('%s' % js)

def get_last_alert():
    """
    Gets the last alert message.  This command MUST be preceeded by Prep Alert
    """
    seleniumlib = BuiltIn().get_library_instance('Selenium2Library')
    return seleniumlib.execute_javascript('return lastAlert')

