# Robot-framework
FarmRise automation framework helps in automating all user scenarios and covers following types of tests.
1. Functional test(UI)
2. API tests
3. Performance tests
4. Stability tests
5. Localization tests

FarmRise automation framework from here on addressed as fr-automation is build up on using following tools and technologies.
 - Appium
 : Appium is an open source automation testing framework for use with native and hybrid mobile apps. It aims to be language and framework agnostic—meaning it can work with any language and testing framework of your choice
 
 - Python (programing language in use)
 
 - Robot framework
 : Robot framework consists of a set of tools, techniques and abstract rules; its job (besides allowing to write automated test cases) is simplifying the test automation process. In practice, Robot is a modular test automation framework that has the capability to interact with 3rd party libraries and functions.
 
 
 Usage:
 Currently can be used via terminal/ command line for execution. like
 robot  -d [path/to/store/results] [testfile/suite] 
 ex: robot -d Results tests/functional_tests.robot 

Dockerized all the environment and added emulators for continous testing cycle implementation as per architecture presented.


Wiki pages of this project contains files explaining about this projects architecural implmentation and also other important QA tasks/implementations like Continous testing process (CICD) integration into product CICD flow.
