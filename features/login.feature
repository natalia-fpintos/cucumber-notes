Feature: Login Screen

  Scenario: An existing user logs into the website
     Given the server is running
      When the user logs in with user admin and password admin
      Then the page will respond with 200
      And the dashboard page will load
      