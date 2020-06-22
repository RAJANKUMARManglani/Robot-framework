import os
import logging
import time

from appium.webdriver.appium_service import AppiumService

appium_service = AppiumService()


def get_Android_Home():
    print("checking ANDROID_HOME is defined in the system..")
    if os.getenv("ANDROID_HOME") is None:
        print("Android home is not defined..")
        raise RuntimeError("Define android home for the system to work...")
    else:
        print("Android Home is defined..Continuing with connection settings..")


def start_appium_session():
    print("starting appium server...")
    logging.info("starting appium server session!")
    appium_service.start()
    time.sleep(1)


def stop_appium_session():
    print("starting appium server...")
    logging.info("starting appium server session!")
    appium_service.stop()
    time.sleep(1)


def get_capabilities():
    pass