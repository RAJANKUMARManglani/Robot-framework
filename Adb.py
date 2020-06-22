import os
import logging


class Adb:

    def __init__(self, device_id):
        self.device_id = device_id

    def push_file(self, path_filename, device_path):
        logging.info("pushing file into device via adb...")
        if device_path is None:
            cmd = os.popen("adb -s "+self.device_id+" push "+path_filename+" \\sdcard\\")
        else:
            cmd = os.popen("adb -s " + self.device_id + " push " + path_filename + " " + device_path)
        logging.info(cmd.read())

    def pull_file(self, path_filename):
        logging.info("pulling file from device via adb...")
        cmd = os.popen("adb -s " + self.device_id + " pull " + path_filename + " \\sdcard\\")
        logging.info(cmd.read())

    @staticmethod
    def get_connected_devices():
        logging.info("getting connected devices list ...")
        device_list = os.popen("adb devices").read().split("\n")
        device_list = [i.replace("\tdevice", "") for i in device_list if "\tdevice" in i]
        if len(device_list) == 0:
            raise RuntimeError("No connected devices, please check and retry the execution...")
        elif len(device_list) == 1:
            return device_list[0]
        elif len(device_list) > 1:
            return device_list

    def open_app(self, app_package = '', app_activity = ''):
        print("opening application with package name : ", app_package)
        cmd = os.popen("adb shell am start "+app_package+" "+app_activity)
        if "Error" not in cmd.read():
            print("Application started via abd successfully..")
        else:
            raise RuntimeError("opening app using app package and app activity failed..")

    def press_recent_apps_button(self):
        print("Pressing on recent apps button using adb...")
        os.system("adb -s "+self.device_id+" shell input keyevent KEYCODE_APP_SWITCH")

    def get_android_version(self):
        logging.info("getting device android version!")
        cmd = os.popen("adb -s "+self.device_id+" shell getprop ro.build.version.release").read()
        try:
            version = int(cmd)
            if isinstance(version, int):
                logging.info(" android version is :", version)
                return version
            else:
                logging.info("android version is not an integer.. please check command result..")
        except Exception:
            raise ValueError("No version number returned while adb querying..")

    def install_app(self, app_path):
        logging.info("installing application via adb..")
        cmd = os.popen("adb -s "+self.device_id+" install "+app_path).read()
        if "Success" in cmd:
            logging.info("app successfully installed via adb..")
        else:
            logging.info("app failed to install via adb command..")
            raise RuntimeError("Failed with application installation.")

    def uninstall_app(self):
        pass

    @staticmethod
    def close_app():
        logging.info("opening application with package name : ")
        for i in range(5):
            os.popen("adb shell input keyevent 4")
        print("Application closed via abd successfully..")

    @staticmethod
    def kill_server():
        logging.info("killing adb server...")
        os.popen("adb kill server")

    @staticmethod
    def start_server():
        logging.info("starting adb server...!!")
        os.popen("adb start-server")

    def reboot_adb(self):
        pass

    def logcat(self):
        pass

    def make_a_call(self):
        pass

    def grant_app_permission(self, package_name, permission):
        pass

    def reset_app_permission(self, package_name):
        pass

    def revoke_app_permission(self, package_name, permission):
        pass

    def input_text(self, text):
        pass


if __name__ == '__main__':
    # adb = Adb("192.168.0.154:5000")
    x = Adb.get_connected_devices()
    print("devices are >>>", x)
    print(type(x))

