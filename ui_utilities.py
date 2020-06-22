import os
import Libraries.config as config


def clear_all_apps(deviceName):
    if deviceName not in config.dev_clear_app.keys():
        raise ValueError("given device name is not found in the required list of devices..")
    else:
        clear_apps_type = config.dev_clear_app.get(deviceName)
        print("clearing all apps from background ...")


def clear_apps_stock_android():
    print("clearing apps for stock android device type..")


class Uiclass:

    def __init__(self):
        pass
