#!/bin/bash

# create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate

# install all dependencies
pip install -r requirements.txt

# initialize db
python -c "from app import db, app; app.app_context().push(); db.create_all()"

# start the application
python app.py
