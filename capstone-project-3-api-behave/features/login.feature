Feature: Verify user login through the API

  Scenario: Valid demo account
    Given the API client is ready
    When I verify the valid demo account
    Then the API response code is 200
    And the API message is "User exists!"

  Scenario: Invalid account
    Given the API client is ready
    When I verify an invalid account
    Then the API response code is 404
    And the API message is "User not found!"