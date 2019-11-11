# CarRental

Example API for practice in implementing automated tests (specifically BDD feature files)

## Usage

- Run server:
    > python manage.py runserver

    Access the server in your browser:
    > http://localhost:8000/
    
## TASK

1. Depending on whether you're working with your colleagues for this task, you can either: 
    1. fork the repository to your github account so you can make changes against your forked repository and it won't affect your colleagues. 
    2. Alternatively you can work together (peer programming is a viable programmming technique that helps lots of developers) and encourages learning workflow amongst your colleagues (great reality simulation.)

2. Setup the repository:
    ## Setup

    1. clone repository: 
        > git clone git@github.com:chrismodus/carrental.git && cd carrental
    1. create a virtual environment for the repository

    1. install requirements
        > pip install -r requirements.txt

3. Write behave-django tests 
    ### Automated Testing
    No automated tests have been implemented.
    The features to test against are found in ./BDD/features/ 

    1. To setup behave-django in a django project follow this guide: https://behave-django.readthedocs.io/en/latest/installation.html

    1. Create a steps directory in ./BDD/features/ and place the step code for each feature in there.
        Run behave-django tests using:
        > python manage.py behave {path_to_feature}
        
    2. Commit your changes to the repository and push once you've implemented the step logic.


