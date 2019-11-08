Feature: Rent a car

    Scenario Outline: Successfully rent a car
        Given the following car exists:
        | name | brand    |
        | E280 | Mercedes |
        And the following rent payload data:
        | name | brand    | rentee    |
        | E280 | Mercedes | <rentee>  |
        When a POST is made to the /rent/ endpoint
        Then the car has been rented out by <rentee>
    
    Examples:
    | rentee | 
    | Chris  |

    Scenario: Rent a non-existing car
        Given the following rent payload data:
        | name   | brand    | rentee  |
        | CLA200 | Mercedes | chris   |
        When a POST is made to the /rent/ endpoint
        Then a 404 is returned
