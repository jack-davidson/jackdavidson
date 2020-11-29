# jackdavidson
personal website and blog

This is my personal website and blog where I post about technology related
subjects.

# installation procedure
```bash
$ git clone https://github.com/jack-davidson/jackdavidson.git
$ cd jackdavidson
$ ./tools/setup.sh
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

# reminders!
when developing and deploying, you need to make sure that the secret key is
never added to version control. You must `cd` into the `src/` directory and run
`../tools/generate_secret_key.py > secret_key.txt`. A more concise version of
this would to be in the root directory of the project and run
`./tools/generate_secret_key.py > src/secret_key.txt`. Do not remove the
secret key from the gitignore because if it gets exposed and used in production,
that would be a serious security vulnerability. It is good to generate a
secret key often.

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
