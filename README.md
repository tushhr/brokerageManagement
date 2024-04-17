# Why this project?
This project was developed solely to support my dad's business. <br>
It's a very basic webapp, with minimum required functionalities, just to get up & running! <br>
In future I might extend this project to include different functionalities, but for now, I'm trying keeping this as simple as possible.

## Requirements
- Django 4.2
- Python 3.8

## Setup
- Fork & Clone the repo.
- Change the directory to `brokerageManagement`
- Install virtualenv `pip install virtualenv`
- Create a virtual environment `virtualenv env`
- Activate the env: `env\Scripts\activate`
- Install the requirements: `pip install -r requirements.txt`
- Make migrations `py manage.py makemigrations`
- Migrate the changes to the database `py manage.py migrate`
- Create admin Using `py manage.py createsuperuser`
- Run the server `py manage.py runserver`
- Cheers!
