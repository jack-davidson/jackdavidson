#!/usr/bin/env sh

# setup.sh:
#
# setup a django development environment for jackmaverickdavidson

cd src
pip install virtualenv
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
./../tools/generate_secret_key.py > secret_key.txt
./manage.py makemigrations
./manage.py migrate

printf "\n\033[31m**\033[0m\033[32m You are now ready to start development or \
run the django development server with ./manage.py runserver (make sure you are\
in the /src directory)\033[0m\033[31m**\033[0m\n\n"
