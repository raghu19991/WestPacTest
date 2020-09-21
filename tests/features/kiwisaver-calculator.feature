Feature: Test Calculator Functionality
  Tests below verify the help icon texts and also calculator logic for different use cases

  @Major
  Scenario: Validate information icons on all fields
    Given I navigate to Kiwisaver Calculator Page
    When I Click information icon besides Current age
    Then message “This calculator has an age limit of 18 to 64 years old.” is displayed below the Current age field

  @Major
  Scenario: Employed Kiwisaver projected balance at retirement
    Given I navigate to Kiwisaver Calculator Page
    When I populate calculator with below fields
    | Current age | Employment status | Salary or wages per year (before tax) | KiwiSaver member contribution | Current KiwiSaver balance | Voluntary contributions | Frequency | Risk profile | Savings goal at retirement|
    | 30          | Employed          | 82000                                 | 4%                            |                           |                         |           | Growth       |                           |
    And I click button View your KiwiSaver retirement projections
    Then Projected balance at retirement is shown on the screen as 709,640

  @Major
  Scenario: Self-Employed Kiwisaver projected balance at retirement
    Given I navigate to Kiwisaver Calculator Page
    When I populate calculator with below fields
      | Current age | Employment status | Current KiwiSaver balance | Voluntary contributions | Frequency   | Risk profile | Savings goal at retirement|
      | 45          | Self-employed     | 100000                    | 90                      | Fortnightly | Balanced     | 290000                    |
    And I click button View your KiwiSaver retirement projections
    Then Projected balance at retirement is shown on the screen as 464,743

  @Major
  Scenario: Not-Employed Kiwisaver projected balance at retirement
    Given I navigate to Kiwisaver Calculator Page
    When I populate calculator with below fields
      | Current age | Employment status | Current KiwiSaver balance | Voluntary contributions | Frequency   | Risk profile | Savings goal at retirement|
      | 55          | Not employed      | 140000                    | 10                      | Annually    | Conservative | 200000                    |
    And I click button View your KiwiSaver retirement projections
    Then Projected balance at retirement is shown on the screen as 239,765
