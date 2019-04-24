# Other features

## Scenario Outlines

When we want to test the same scenario but with different values, we can define a scenario ourline and use placeholders to define different variants of the same scenario.

To begin with, rather than define a __Scenario__ at the top, we have to define it as a __Scenario Outline__.

Then, we can define variables in the step, and one or more __Examples__ table with all the values for these variables at the bottom. Each row will be a different scenario:

```cucumber
Scenario Outline: Blenders
   Given I put <thing> in a blender,
    When I switch the blender on
    Then it should transform into <other thing>

 Examples: Food
   | thing         | other thing |
   | strawberries  | smoothie    |
   | chickpeas     | hummus      |

 Examples: Consumer Electronics
   | thing         | other thing |
   | iPhone        | toxic waste |
   | Galaxy Nexus  | toxic waste |
```

## Step data

We can also provide data associated with a step, this can be done in many ways:

  * __Text block__: If we define a text block wrapped between `"""`, this data will be available for the step in `context.text`.

  ```
  Scenario: some scenario
    Given a sample text loaded into the frobulator
      """
      Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
      eiusmod tempor incididunt ut labore et dolore magna aliqua.
      """
     When we activate the frobulator
     Then we will find it similar to English
  ```

  * __Table data__: We can provide a table of data after a step, this will be available in `context.table`, and can be accessed as shown below:

  ```
  Scenario: some scenario
    Given a set of specific users
      | name      | department |
      | Barry     | Sales      |
      | Lana      | Sales      |
      | Sue       | Service    |

     When we count the number of people in each department
     Then we will find two people in "Sales"
      But we will find one person in "Service"
  ```

  ```python
  @given('a set of specific users')
  def step_impl(context):
      for row in context.table:
          model.add_user(name=row['name'], department=row['department'])
  ```

  * __Parameters__: We can also provide a parameter for a step, by wrapping a value between double quotes. This will then be available to the step as a parameter for the function it calls. Therefore, we need to define the parameter in the function as well.

  ```cucumber
  Scenario: look up a book
    Given I search for a valid book
     Then the result page will include "success"

  Scenario: look up an invalid book
    Given I search for a invalid book
     Then the result page will include "failure"
  ```

  ```python
  @then('the result page will include "{text}"')
  def step_impl(context, text):
      if text not in context.response:
          fail('%r not in %r' % (text, context.response))
  ```

  (In this example, the __Given__ step will put some data in `context.response`).
  