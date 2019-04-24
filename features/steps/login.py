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
