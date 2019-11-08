Feature: Add cars to inventory

    Scenario: Add car to inventory
        Given the following car payload data:
        | name | brand    |
        | E280 | Mercedes |
        When a POST is made to the /cars/ endpoint:
        Then the car has been added

    Scenario Outline: Add cars to inventory
        Given the following car payload data:
        | name   | brand   |
        | <name> | <brand> |
        When a POST is made to the /cars/ endpoint:
        Then the car has been added

        Examples:
        | name | brand     |
        | E320 | Mercedes  |
        | E450 | Mercedes  |
        | S63 AMG | Mercedes  |
        | 325i | BMW  |
        | GTI8 | VW  |