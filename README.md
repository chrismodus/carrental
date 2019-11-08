# CarRental

Tutorial API to provide testers a platform to work with (repo can be updated with more example tasks)

## Usage

- Run server:
    > python manage.py runserver

    Access the server in your browser:
    > http://localhost:8000/
    
## TASK

1. Fork the repository

2. Setup repository:
    ## Setup

    1. clone repository: 
        > git clone git@github.com:chrismodus/carrental.git && cd carrental
    1. create a virtual environemnt for the repository

    1. install requirments
        > pip install -r requirements.txt

3. Write behave-django tests 
    ### Automated Testing
    No automated tests have been implemented.

    1.To setup behave-django in a django project follow this guide: https://behave-django.readthedocs.io/en/latest/installation.html

    The features to test against are found in ./BDD/features/ 

    1. Create a steps directory in ./BDD/features/ and place the step code for each feature in there.
        Run behave-django tests using:
        > python manage.py behave {path_to_feature}
    2. Commit your changes to the repository and push once you've implemented the step logic.


