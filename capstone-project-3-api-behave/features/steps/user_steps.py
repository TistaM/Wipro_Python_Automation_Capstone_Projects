from uuid import uuid4

from behave import given, when

from api.client import APIClient


@given("a new temporary user")
def step_new_user(context):
    context.client = APIClient()
    context.user_deleted = False
    context.user = {
        "name": "Capstone Test",
        "email": f"capstone-{uuid4().hex[:12]}@example.com",
        "password": f"Test-{uuid4().hex[:16]}!",
        "title": "Mr",
        "birth_date": "1",
        "birth_month": "1",
        "birth_year": "2000",
        "firstname": "Capstone",
        "lastname": "Test",
        "company": "Demo",
        "address1": "Test Address",
        "address2": "Test Address",
        "country": "India",
        "zipcode": "100001",
        "state": "Test State",
        "city": "Test City",
        "mobile_number": "9000000000",
    }


@when("I create the user through the API")
def step_create_user(context):
    context.result = context.client.create_user(context.user)
    context.user_created = context.result.get("responseCode") == 201


@when("I retrieve the user through the API")
def step_get_user(context):
    context.result = context.client.get_user(context.user["email"])


@when("I update the user's name through the API")
def step_update_user(context):
    context.user["name"] = "Capstone Updated"
    context.result = context.client.update_user(context.user)


@when("I delete the user through the API")
def step_delete_user(context):
    context.result = context.client.delete_user(
        context.user["email"], context.user["password"]
    )
    context.user_deleted = context.result.get("responseCode") == 200