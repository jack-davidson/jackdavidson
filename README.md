# jackdavidson
personal website and blog

This is my personal website and blog where I post about technology related
subjects.

# installation
To install and run this on your own machine using the django development server,
first clone this repository:
`git clone https://github.com/jack-davidson/jackdavidson.git`

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

```
jackdavidson
    ├── README.md
    ├── blog
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── ...
    │   ├── models.py
    │   ├── static
    │   │   ├── script
    │   │   └── style
    │   ├── templates
    │   │   └── blog
    │   │       ├── blog.html
    │   │       └── index.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── core
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── ...
    │   ├── models.py
    │   ├── static
    │   │   └── core
    │   │       ├── img
    │   │       │   └── devicon.png
    │   │       ├── script
    │   │       └── style
    │   ├── templates
    │   │   └── core
    │   │       └── index.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── db.sqlite3
    ├── jackdavidson
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── requirements.txt
    ├── secret_key.txt
    ├── static
    │   ├── img
    │   ├── script
    │   │   ├── base.js
    │   │   └── toggle.js
    │   └── style
    │       └── base.css
    └── templates
        └── base.html
```
