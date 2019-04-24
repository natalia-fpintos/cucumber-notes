# Steps

## Types

The steps defined in a BDD `feature` file must include:

  * __Given__ step(s), which define the state in which we put the system before the user can begin the interactions. This is mainly the setup of the scenario.

  * __When__ step(s), these describe the actions that the user takes to interact with the system.

  * __Then__ step(s), these provide the outcomes that we expect based on the interactions.


Additionally, we can include __And__ or __But__ steps, these are interpreted as the same step type of the preceeding step (for example, the __And__ step in the example bellow is interpreted as a __Then__, so the step definition should be decorated with `@then`).

```cucumber
Feature: Login Screen

  Scenario: An existing user logs into the website
     Given the server is running
      When the user logs in with user admin and password admin
      Then the page will respond with 200
      And the dashboard page will load
```


## Definition

We define the steps in a python file, decorating a function with the respective step (i.e. `@given`). If we want to use a step for many different types of steps, for example, a step that can be used as __Given__ or as __Then__, we can always use the generic `@step` decorator.
