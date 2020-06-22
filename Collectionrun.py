import os
import subprocess
import logging

report_path = '//Users//rajan.kumar.manglani//Documents//All important jars//fr-automation-framework-master//Results'
collection_json_path = '//Users/rajan.kumar.manglani//Documents//All important ' \
                       'jars//fr-automation-framework-master//Appsource//TestData//Testcase_FarmriseApi' \
                       '.postman_collection' \
                       '.json '


def execute_api(url):
    subprocess.call('start', shell=True)
    output = subprocess.getoutput("newman run " + url + " ")
    print(output)
    logging.info("Collection run successfully")
    os.popen("newman run " + url + " -r html --reporter-html-export '" + report_path + "/overviewReport.html' ")
    logging.info("Overview report is published in folder")
    os.popen("newman run " + url + " -r htmlextra --reporter-htmlextra-export '" + report_path + "/detailedReport"
                                                                                                 ".html' ")
    logging.info("Detailed report is published in folder")
    if output.find("failure"):
        print("Test case failed >> one of api in collection assertion failed")
        return True

    else:
        print("Test cases of collection are passed >> all Api are successfully passing")
        return False


def execute_json_collection(json):
    subprocess.call('start', shell=True)
    os.chdir('/Users/rajan.kumar.manglani/Documents/All important '
             'jars/fr-automation-framework-master/Appsource/TestData')
    output = subprocess.getoutput('newman run ' + json + '')
    print(output)
    logging.info("Collection run successfully")
    os.popen("newman run " + json + " -r html --reporter-html-export '" + report_path + "/overviewReport1.html' ")
    logging.info("Overview report is published in folder")
    os.popen("newman run " + json + " -r htmlextra --reporter-htmlextra-export '" + report_path + "/detailedReport1"
                                                                                                  ".html' ")
    logging.info("Detailed report is published in folder")
    if output.find("failure"):
        print("Test case failed >> one of api in collection assertion failed")
        return True

    else:
        print("Test cases of collection are passed >> all Api are successfully passing")
        return False


class RunCollection:
    uri = 'https://www.getpostman.com/collections/65e1541ba4c74f7196f2'

    def __init__(self, uri):
        self.uri = uri


p1 = RunCollection("https://www.getpostman.com/collections/65e1541ba4c74f7196f2")
execute_api('https://www.getpostman.com/collections/65e1541ba4c74f7196f2')
execute_json_collection('Testcase_FarmriseApi.postman_collection.json')
