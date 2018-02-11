Feature: URLs shortening
  Scenario: Asking for non existing link should fail
    Given a service
    Then asking for non-existing-key gives 404

  Scenario: Save link and ask for it
    Given a service
    When we try to shorten https://google.com
    Then key should be returned
    Then asking for key redirects to https://google.com
