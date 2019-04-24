# Behave - BDD with Python

Behave is a tool to do Behaviour-Driven Development in Python.


## 1. Installation

We can easily install behave with `pip`:

```
$ pip install behave
```

## 2. Create a feature file

We begin by creating a directory in our repo, called `features`. Then we can add our test files in this folder, which will have the extension `.feature`, i.e. `login.feature`.

Inside this file, we can begin to write our behavioural test. These have the following format:

```cucumber
Feature: Login Screen

  Scenario: An existing user logs into the website
     Given the server is running
      When the user logs in with user admin and password admin
      Then the page will respond with 200
      And the dashboard page will load
```

## 3. Define the steps

The different lines defined in the scenario are called *steps*. Each of these will have a function linked to it, which will execute some code to make the step pass or fail. We define these functions by creating a directory inside `features`, we should call this new directory `steps`. Inside the `features/steps` directory we will create a python file for our feature, i.e. `login.py`.

The python file will contain functions for our steps, with the following format:

```python
from behave import *

@given('the server is running')
def server_running(context):
    assert True is True

@when('the user logs in with user admin and password admin')
def login(context):
    assert True is not False

@then('the page will respond with 200')
def page_response(context):
    assert context.failed is False

@then('the dashboard page will load')
def page_loads(context):
    assert context.failed is False
```

## 4. Running the tests

In order to run the tests, we simply have to call `behave`. This will run all our feature tests:

```
$  behave
Feature: Login Screen # features/login.feature:1

  Scenario: An existing user logs into the website           # features/login.feature:3
    Given the server is running                              # features/steps/login.py:3 0.000s
    When the user logs in with user admin and password admin # features/steps/login.py:7 0.000s
    Then the page will respond with 200                      # features/steps/login.py:11 0.000s
    And the dashboard page will load                         # features/steps/login.py:15 0.000s

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
4 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.001s
```
