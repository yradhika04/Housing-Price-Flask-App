@echo off

:: create and activate the virtual environment
python -m venv venv
call venv\Scripts\activate

:: install all dependencies
pip install -r requirements.txt

:: initialize db
python -c "from app import db, app; with app.app_context(): db.create_all()"

:: start the application
python app.py
