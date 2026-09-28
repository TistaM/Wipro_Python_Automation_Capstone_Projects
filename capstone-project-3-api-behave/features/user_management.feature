Feature: Manage a temporary user account

  Scenario: Create, retrieve, update, and delete a user
    Given a new temporary user
    When I create the user through the API
    Then the API response code is 201
    When I retrieve the user through the API
    Then the API response code is 200
    When I update the user's name through the API
    Then the API response code is 200
    When I delete the user through the API
    Then the API response code is 200