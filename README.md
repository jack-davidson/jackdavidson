# jackdavidson
personal website and blog

This is my personal website and blog where I post about technology related
subjects.

# installation
```
$ git clone https://github.com/jack-davidson/jackdavidson.git
$ cd jackdavidson
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 -c "from django.core.management import utils;
  print(utils.get_random_secret_key())" > secret_key.txt
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
```
and DONE! You will have to do additional setup for using the admin
interface such as creating a superuser to manage the website, the
instructions for this are documented in the django documentation.

# technologies used
I am using:
- Python + django for the backend
- SQLite for the database
- HTML + CSS + Vanilla Javascript for the frontend

the acronym for this is:
**L** inux
**N** ginx
**S** qlite
**P** ython

LNSP stack, I don't know if this is a thing but this is what my stack's acronym
is.

# project structure

As django is a very structured framework, developers need to make sure that they
establish a system to keep your project organized. Django's template system
allows the developer to use inheritance to write less code. This inheritance
also must be used in css to keep your project optimally organized.

For css classes and ids that are needed by multiple apps, the stylesheets should
be placed in the global /static/style directory. If a stylesheet is only needed
by one app that should be placed in the <app>/static/style directory.

Stylesheets should include a minimal amount of classes and rules and all
rules in a stylesheet should be related to each other. Otherwise, make a
separate stylesheet for them.
