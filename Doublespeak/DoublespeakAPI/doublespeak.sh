#!/usr/bin/env bash
find . -path "/DoublespeakAPI/API/migrations/*.py" -not -name "__init__.py" -delete; #deletes all of the .py files in the migrations directory except for the __init__.py file.
find . -path "/DoublespeakAPI/API/migrations/*.py"  -delete; #deletes all of the .pyc files in the migrations directory.
rm db.sqlite3; #deletes the database file.
python manage.py makemigrations; #creates the migration.
python manage.py migrate; #runs the migration.  This will delete all of the data in your database.
