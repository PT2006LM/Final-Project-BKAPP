# Final-Project-BKAPP


### Project setup
Install dependencies (recommended in a virtual environment) via
> pip install -r requirements.txt

Since this project use weasyprint which require GTK, install the dependency via the [document's instruction](https://weasyprint.readthedocs.io/en/latest/install.html).

This project connects to mysql database. Therefore, in mysql server, create a database namely *foodstore* (or change the name in database's setting in `settings.py`).
Then run `python manage.py migrate`


### Run project in development server
Run command `python manage.py runserver` and access to `localhost:8000`
