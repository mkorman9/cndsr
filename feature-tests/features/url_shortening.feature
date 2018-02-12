Feature: URLs shortening
  Scenario: Asking for non existing link should fail
    Given a service
    Then asking for non-existing-key gives 404

  Scenario: Save link and ask for it
    Given a service
    When we try to shorten https://google.com
    Then key should be returned
    Then asking for key redirects to https://google.com

  Scenario: Protocol prefix should be automatically appended
    Given a service
    When we try to shorten google.com
    Then key should be returned
    Then asking for key redirects to http://google.com

  Scenario: URL without dot should be rejected
    Given a service
    When we try to shorten google
    Then request should be rejected

  Scenario: URL containing reserved network address should be rejected
    Given a service
    When we try to shorten http://192.168.2.1/
    Then request should be rejected
