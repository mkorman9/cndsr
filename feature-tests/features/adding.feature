Feature: Adding integers
  Scenario: Two integers should be added properly
    Given a service
    When we request /add/3/7 endpoint
    Then 10 should be returned
