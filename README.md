# Notes about BDDs and Cucumber tests 🥒

1. [Behave - BDD with Python](https://github.com/alysanne/cucumber-notes/blob/master/behave-python.md)
2. [Steps](https://github.com/alysanne/cucumber-notes/blob/master/steps.md)
3. [Context](https://github.com/alysanne/cucumber-notes/blob/master/context.md)
4. [Other features](https://github.com/alysanne/cucumber-notes/blob/master/other-features.md)


## What is BDD?

- BDD stands for Behaviour Driven Development
- We use BDD to test to make the requirements clear during testing, this also helps understand how the application or specific features should work when someone needs to refactor or work on them for the first time
- BDDs are written in plain English and usually describe a situation where a user interacts with the application, its behaviour and outcomes


## What is `cucumber`?

- Cucumber is a tool that facilitates writting BDDs
- It allows the users to create a `.feature` file which contains the tests step by step, written in plain English
- Then, each step is linked to a function in a separate file, and this function should execute to fulfill the definition of the step (for example, if a step says `"Given I am connected to the server"`, then the function should connect to the server
- As cucumber can be used with many different languages, there is a specific tool that allows us to write the backing code for our steps in Python, this tool is `behave`
