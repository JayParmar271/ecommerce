## Requirements
- Python 3.8+ [https://www.python.org/downloads/]

## Project setup
## 1. Create virtual environment

    python3 -m venv venv

## 2. Activate virutal environment

### For windows
    source <virtual_environment_dir>/venv/Scripts/activate

### For ubuntu
    source <virtual_environment_dir>/venv/bin/activate

## 3. Install python dependencies
    python manage.py -r requirements.txt

## 4. Run project

### Run migrations
    python manage.py makemigrations
    python manage.py migrate

### Run django server
    python manage.py runserver

### Create super user
    python manage.py createsuperuser
    
