Feature: Printing Hello world through HTTP
  Scenario: Request and validate response
    Given a service
    When we request / endpoint
    Then Hello world should be returned
