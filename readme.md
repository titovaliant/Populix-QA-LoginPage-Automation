## Automation-Testing [Populix - QA_TEST]
Automation Using Selenium Hybrid Framework
(Python, Selenium, PyTest, Page Object Model, HTML Reports)

Prepared by:
**Tito Valiant Muhammad - QA Engineer Candidate**

### What is Framework?
framework is an organized way maintaining automation files.

In the framework all the files will communicate each other to perform certain task.

### Objective/Goals:
1). Re-usuability

2). Maintainability

### Concepts Included

1). Built-in Frameworks
    
    pytest

2). Customized/User defined frameworks

    Data driven framework, Keyword driven framework, Hybrid driven framework

## 1. A detailed test cases 
You can see all the Manual Testing Documentation by following this link below:

<a href="https://docs.google.com/spreadsheets/d/1hgLmoNVobe1XqgH3Cte2qNL4rGBdz0infacAozNEuqk/edit?usp=sharing">TestCases-Populix-LoginPage-Tito</a>

## 2. Requirements and Tools

In order to utilise this project you need to have the following installed locally:

* Python
* Chrome and Chromedriver
* Selenium : Selenium Webdriver
    
    On Terminal use this command (inside the SQAlogin Populix folder):
    ```
    $ pip install selenium
    ```
* Pytest : Python UnitTest framework
    
    On Terminal use this command (inside the SQAlogin Populix folder):
    ```
    $ pip install -U pytest
    ```
* pytest-html : PyTest HTML Reports
    
    On Terminal use this command (inside the SQAlogin Populix folder):
    ```
    $ pip install pytest-html
    ```
    ```
    $ pip install pytest-metadata
    ```
* Openpyxl : MS Excel Support
    
    On Terminal use this command (inside the SQAlogin Populix folder):
    ```
    $ pip install openpyxl
    ```
* Virtual Env Python:
    
    On Terminal use this command (inside the SQAlogin Populix folder):
    ```
    $ pip install virtualenv`
    ```
## 3. Reporting

Reports for each module are written into their respective `/Reports` directories after a successful run with HTML Reports format.

Log tests result in a .log report for each feature/testCases in folder `/Logs/testing_data.log`.

In the case of test failures, a screen-shot of the UI at the point of failure is embedded into the report in folder `/Screenshots`.

## 4. Usage/How to Run

The project is broken into separate Folder and Package.

### all testCases/Modules:
To run all modules, navigate to `/testCases` directory and run:

`$ pytest  -v --html=Reports\report_ALL_TestCases.html testCases --self-contained-html`

*NOTE*: They will also generate a security risks HTML report in `Reports\report_ALL_TestCases.html`

### valid test:
To run Valid Login tests only, navigate to `/testCases` directory and run:

`$ pytest  -v --html=Reports\report_valid_Test.html testCases\test_login_valid.py --self-contained-html`

*NOTE*: They will also generate a security risks HTML report in `Reports\report_valid_Test.html`

### invalid test:
To run Invalid Login tests only, navigate to `/testCases` directory and run:

`$ pytest  -v --html=Reports\report_Invalid_Test.html testCases\test_login_invalid.py --self-contained-html`

*NOTE*: They will also generate a security risks HTML report in `Reports\report_Invalid_Test.html`

### function test:
To run Function tests only, navigate to `/testCases` directory and run:

`$ pytest  -v --html=Reports\report_function_Test.html testCases\test_login_function.py --self-contained-html`

*NOTE*: They will also generate a security risks HTML report in `'Reports\report_function_Test.html'`

### *POPULIX RECRUITER NOTE*: 

B. Create a Bash Script for login function with following requirements is available inside this file. I Name it with `login.sh`

C. Explain briefly between test suite, test case, and test step! is available inside this file. I Name it with `tes teori POPULIX bab C & D.txt`

D. What's the difference between regression test and non-regression test? is available inside this file. I Name it with `tes teori POPULIX bab C & D.txt`
