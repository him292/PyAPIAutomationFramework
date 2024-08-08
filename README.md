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

- Install Jenkins - Jenkins download (ZSH commandline: Go to the jenkins war path and then execute-> java -jar jenkins.war --enable-future-java)
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

### If you checked "Role Based security" from within the Security tab
- then, you can Manage role and assign roles
- Assign these created roles to your users

### JENKINS Pipeline
- is a simple test file (Jenkinsfile) which can be committed to a project's source control repository
- A pipeline is basically is sequential process of performing tasks

### Continuous Integration: Automatically integrate code changes from multiple developers, ensuring that the codebase is always in a releasable state.
### Continuous Delivery: Automate the process of delivering code to production or staging environments, ensuring faster and more reliable releases.

### Why Pipline: Pipelines are defined in a jenkinsfile using a domain specific language (dsl) based on groovy
- uses code to defin pipelines makes them easy to reuse (maintainable)
- customizable: can be customized from simple build-test-deploy workflows to complex multi-stage processes
- Extensible: rich ecosystem of plugins that cna be integrated with pipelines
- Logging/Reporting: provide detailed logs and build reports, makes easier to diagnose issues
- Visualization: provides a graphical representation of the pipeline stages and steps
- Parallel execution: allows parallel execution of tests simultaneously
- Scalability: Distributed builds
- Integration with other tools: integrates woth wide variety of devOps tools like Git, docker, kubernetes etc

- jenkins pipeline example:

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // Add build steps here
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Add test steps here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Add deploy steps here
            }
        }
    }
}

In the above code:
- Node is a machine which is part of the Jenkins environment and is capable of executing a pipeline
- Stage defines a conceptually distinct subset of tasks performed through the entire pipeline (Ex Build - test- deploy)
- Step: This tells jenkins what to do at a particular point in time


### Jenkins Pipeline Vs Freestyle Job
- For ex: You have different tasks to do: 
  - Setup environment
  - Run the test cases
  - Publish the test cases
  - Send the notifications
  - Send the reports
- If all of the above needs to e automated, then we dont have a good or flexible mechanism with "Freestyle Job", so will
- go with Jenkins Pipeline where I can add my stages like Build, test, deploy etc


### JENKINS CLI (Command Line)
- Why needed? - If you want to create or build a job via cmd
- localhost:8080/cli
- If you want to know all the cli commands, then go to
  - Manage jenkins -> Jenkins CLI

- To use CLI, run the cli jar (http://localhost:8080/jnlpJars/jenkins-cli.jar) and run as follows (chck other commands from manage jenkins):
  - java -jar jenkins-cli.jar -s http://localhost:8080/ help
- Now, go to command line
  - go to the path where you have downloaded the CLI.jar
  - type "java -jar jenkins-cli.jar -s http://localhost:8080/ build "pipeline_name"
    - now, if you run like this, then in the console output, it'll say its run by an anonymous user
    - if you want to add the user context, then go to the userprofile icon in jenkins -> click configure
      - click and generate API token. Now use this token within your job (while creation)
      - Command: java -jar jenkins-cli.jar -s http://localhost:8080/ -websocket -auth USER: "API Token" create-job "job name"


### How to create Jenkins Job with Parameters (need to watch video again)

### Send reports/notifications, attach logs via email from Jenkins (how to setup SMTP server)
- Need to have a email account (with less security so that Jenkins can communicate with the SMTP protocol)
  - Then go to, "https://myaccount.google.com/u/2/lesssecureapps" and activate the "less secure account" toggle
    - If you're not able to activate it, check your security settings
  - Go to Jenkins -? manage jenkins
  - go to configure system -> email notification -> advanced
    - add username/password, add SMTP server "smtp.gmail.com"
    - click use SSL and TLS
    - add port (465)
    - then test config and check email ( a test)
  - Once this is setup, then you need to setup this in your Jenkins pipeline/job
    - Go to configure
      - Post build actions
        - click on Email notfication
      - Also, you can add one plugin (Extended Email notification)
        - This allows to customize the Subject, body etc of the email
z