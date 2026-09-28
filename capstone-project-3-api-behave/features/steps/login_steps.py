import os

from behave import given, then, when

from api.client import APIClient


@given("the API client is ready")
def step_client_ready(context):
    context.client = APIClient()


@when("I verify the valid demo account")
def step_valid_login(context):
    context.result = context.client.verify_login(
        os.environ["AE_TEST_EMAIL"],
        os.environ["AE_TEST_PASSWORD"],
    )


@when("I verify an invalid account")
def step_invalid_login(context):
    context.result = context.client.verify_login(
        "not-a-user@example.invalid",
        "incorrect-password",
    )


@then("the API response code is {expected:d}")
def step_response_code(context, expected):
    assert context.result["responseCode"] == expected, context.result


@then('the API message is "{expected}"')
def step_message(context, expected):
    assert context.result["message"] == expected, context.result