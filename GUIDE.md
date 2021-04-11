
## How To Run The App
* First, install all requirements by running the following command:
  > pip3 install -r requirements.txt
  
* Go through [database setup](database_setup.md).
* After successfully setting up the database and changing the database credentials
in the [Configurations File](config.py), execute the following command:
  > python3 app.py
  
* The application by default is exposed through port 5000. This can be modified in [Application file](app.py).
## How To Send Request
* We advise testers to use [Postman](https://www.postman.com/downloads/).
* All request should be sent in the format: "_URL:/Port/Endpoint {Payload, If any}_"
E.g.
  > http://127.0.0.1:5000/guide
  > 
    And the request method should be specified.

# Endpoints
1. Registering a new RBS user.
    * Method: POST
    * Endpoint: /user/add
    * Payload: userId, firstname, lastname, password
    >http://127.0.0.1:5000/user/add?userId=110&firstname=Thor&lastname=Odin&password=1234