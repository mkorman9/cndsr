Feature: Adding integers
  Scenario Outline: Two integers should be added properly
    Given a service
    When we request /add/<x>/<y> endpoint
    Then <sum> should be returned

    Examples:
      |  x  |  y  | sum |
      |  1  |  1  |  2  |
      |  2  |  1  |  3  |
      |  5  |  5  |  10 |
