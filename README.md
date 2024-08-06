# Test Stack
- Python 3.12
- Requests - HTTP Requests
- Pytest
- Reporting - Allure, Pytest HTML
- Test Data - CSV, Excel, JSON, Faker
- Parallel execution - x distribute (sdist)
- Adbvance API Test case - JSON test cases

## To install all the above libraries at once, run below query:
pip install requests pytest pytest-html faker pytest-x-dist allure-pytest jsonschema 

Faker is a python library that is used to generate fake data for testing

# to run a test case
pytest tests/crud/test_create_booking.py --alluredir=allure_result -s

# how to clean the allure-reports
allure generate -clean

## JENKINS Notes
- Slave who can run automation whenever you want and email to people
- Build -> Test -> Deploy code
- Trigger

## How to run Jenkins build on Mac

"MAC"
cd "/Library/Frameworks/Python.framework/Versions/3.12/bin/python3"
pip3 install -r requirements.txt "path to python until scripts"
pytest tests\integration\test_crud.py -s -v --html=report.html --alluredir=.\reports 

"Windows"
set path="path to python"
set path=" path to python until scripts"
pip install -r requirements.txt
pytest tests\integration\test_crud.py

## To set the $JAVA_HOME

echo 'export JAVA_HOME=$(/usr/libexec/java_home)' >> ~/.zshrc
source ~/.zshrc

$JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-22.jdk

### Run Jenkins Process

- Install Jenkins - Jenkins download (ZSH commandline: java -jar jenkins.war --enable-future-java)
- Install JDK (pen JDK)
- Install plugins - from manage plugins
  - allure
  - html report
  - python plugin
- Go to tools -> go to JDK -> add path of JDK
- GITHUB - repo ulr: "https://github.com/him292/PyAPIAutomationFramework.git"
- then, click on new item to create a new freestyle project
  - In General: add description
  - Source code management: add git path
  - Build trigger: build periodically (Schedule: cron job Ex: Min Hour DayOfMonth Month DayOfWeek)
  - Build environment: 
  - Build Steps: Add any instruction or command (like check python --version)
  - Post_build Actions: select Generate allure report

- Freestyle Job: Its an unrestricted job. its a simple job

### Other things we can do with Jenkins
- Can add plugins
- Can add users
  - can add access roles/Security
- Can send email notifs