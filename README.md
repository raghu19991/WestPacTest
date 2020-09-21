# Summary
This test Repo consists of automated tests for WestPac Kiwisaver calculator feature as requested.  
The tests are in BDD format in kiwisaver-calculator.feature file.  
The step definitions are in steps folder and Pages folder contains some page specific functions.  
The tests have been executed on Chrome and firefox.The framework is scalable and can be extended as per need.  
The Reports folder contains the Junit report.

# Pre-requisites:
1)Python 3.5 or higher  
Latest versions can be downloaded from https://www.python.org/downloads/  
2)Updated Browsers
3)Adding <Python_dir>,<python_dir>/Lib to environment PATH variable. (if not already there)


# Installation
1)Clone the Project usig git clone https://github.com/raghu19991/WestPacTest.git or using source tree.  
2)In the root directory of the project(WestPacTest) run below command  
pip install -r requirements.txt  
3)Download drivers (chromedriver.exe,geckodriver.exe) and put them in <python_dir>/Lib folder. Make sure that Lib folder is in PATH variable.
  
Check if the drivers installed are compatable with the browser version otherwise please update the browsers or downgrade the drivers. Version specific drivers can be downloaded from https://chromedriver.chromium.org/downloads and https://github.com/mozilla/geckodriver/releases

# Basic Use:
cd <root>/tests  ( cd to tests folder)

behave

# Other Command Line Options:
To get Junit report:  
behave --junit

To run tests based on tags (Major,Minor)  
behave --tags="Major"

To run against different browser  
behave -D browser=chrome  
behave -D browser=firefox

# IDE :
Load the project into any IDE.  
Install Behave plugin.  
Set the run configuration as below :  

Feature files or folders : <project_dir>\tests  
Params(optional)         : -D browser=chrome  
Python Intepreter        : <python_dir\python.exe>

