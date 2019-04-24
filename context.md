# Context

## The context variable

The `context` is a variable that is passed around between the different steps. It's very useful to set data that can be read by future steps in the test.

When `behave` runs a new feature or scenario, it adds a new layer to the context, then, for the duration of that feature/scenario, the context will use that new layer, and then it will be discarded. (Similar to scoped variables defined with `let` in JS).

For example, the scenario bellow will alter the context and pass that value, which will be used by the following steps. After it's done, the context will return to the state it had before the scenario:

```python
@given('I access the login page')
def step_impl(context):
    client = Client("http://127.0.0.1:8080/login/")
    context.response_status = 200

@then('I should receive an OK response')
def step_impl(context):
    eq_(context.response_status, 200)
```

## Default values

The `context` will also have some additional values that are added by `behave`:

  * `context.table`: holds any table data associated with a step.
  * `context.text`: holds any block text associated with a step.
  * `context.failed`: this is set when a step fails, at the root layer of the context.
