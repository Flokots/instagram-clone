# Instagram Clone

An Instagram clone built with Django. 

### Demo
[Instagram Clone]()]

### Author
[Florence Kotohoyoh](https://github.com/Flokots)

### User Stories
1. Sign in to the application to start using.
2. Upload my pictures to the application.
3. See my profile with all my pictures.
4. Follow other users and see their pictures on my timeline.
5. Like a picture and leave a comment on it.

### Technologies and Dependencies Used
* Django
* Python
* Heroku
  
### Project Setup
1. Clone this repository.
2. `cd` into the cloned repository.
3. Create a virtual environment
4. Install the dependencies using:
   ```
   pip install -r requirements.txt
   ```
5. Create the database
   ```
   $ python
   >>> psql;
   >>> CREATE DATABASE database_name;
   ```
6. In the `settings.py` update the database configurations.
7. Make initial migrations 
   ```
   python manage.py makemigrations main
   python manage.py manage.py migrate
   ```
8. Run `python manage.py runserver` to run the application locally. View the app on the `localhost:8000'
9. Run `python manage.py test main` to run the tests.
10. Have fun exploring!
  
### Contributions
Should you notice any bug or  want to add a feature, follow these steps to contribute:
1. Fork this repository.
2. Clone the forked repository.
3. Make changes.
4. Create a pull request.

### Known Bugs
Copy Link button not functional
### Contact
florencekotohoyoh@gmail.com
### License
[MIT](choosealicense.com/licenses/mit)
Copyright (c) 2022
