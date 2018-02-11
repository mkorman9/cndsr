Feature: URLs shortening
  Scenario: Save link and ask for it
    Given a service
    When we try to shorten https://google.com
    Then key should be returned
    Then asking for key redirects to https://google.com
