# Instagram Clone

# author
Mishael Ratemo
 
# Project descriotion
A personal gallery web application to display great images by categories and locations from around the world.

# Live [Demo](https://mismorainsta.herokuapp.com/)

# User story

+ Sign in to the application to start using.
+ Upload my pictures to the application.
+ See my profile with all my pictures.
+ Follow other users and see their pictures on my timeline.
+ Like a picture and leave a comment on it.


## Technologies used
    * BackEnd: * Python - Django
    * FontEnd:  jinja2 , CSS,   Bootstrap
    * Database * PostgreSQL
    * Deployment * Heroku

## Installation / Setup instruction

## Cloning
* Open Terminal {Ctrl+Alt+T}

* git clone ``git@github.com:MishaelRatemo/instagram_clone_django.git``

 + or
 git clone ``https://github.com/MishaelRatemo/instagram_clone_django.git``

* cd instagram_clone_django

* Vs code . or atom . based on the text editor you have.

### The application requires the following installations to operate 
* python3
* virtual environment - see more on how to install virtual on google
* heroku for online deployment.
#### Requirements
+   asgiref==3.5.0
+   backports.zoneinfo==0.2.1
+   beautifulsoup4==4.10.0
+   dj-database-url==0.5.0
+   Django==4.0.3
+   django-bootstrap-v5==1.0.11
+   django-heroku==0.3.1
+   django-registration-redux==2.9
+   gunicorn==20.1.0
+   Pillow==9.0.1
+   psycopg2==2.9.3
+   python-decouple==3.6
+   soupsieve==2.3.1
+   sqlparse==0.4.2
+   tzdata==2021.5
+   whitenoise==6.0.0
### Running the application
Once in the cloned folder run the following commands:-
 * #### create Django environnent
        $  python3 -m venv pip virtual -- creates the virtual for runnning your app      
        $ source virtual/bin/env  -- activate  the virtual
        $ pip install -r requirements.txt - this installs all dependecies necessary for app to run
* #### Setup Configurations and Databases
        $ python3 manage.py makemigrations instagram 

* #### Running the application
        $ python3 manage.py runserver

* #### Running the application
        $ python3 manage.py test instagram

* #### Browse app
        $ 127.0.0.1:8000

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug
* also incase you run it a bug feel free to add or contact

## Contact Information 

If you have any question or contributions and support, please email me at [ratemomishael@gmail.com](ratemomishael@gmail.com)

LinkedIn - [Mishael Ratemo](www.linkedin.com/in/mishael-mosoti-37b786161/)


Portfolio- [Mishael](https://mishaelratemo.github.io/my_portfolio/)
# Licence

Click to  [MIT License](Licence) view

 Copyright (c) 2022 | Mishael Ratemo
