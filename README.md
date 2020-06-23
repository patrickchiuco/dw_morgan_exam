# How to Run
Instructions:
1) Replace the username and password in DWMorgan/dw_morgan/dw_morgan/settings.py with your local postgres username and password.
2) Create a database named dw_morgan_exam in postgres by doing:
	a) sudo -u postgres psql
	b) create database dw_morgan_exam
3) Go to DWMorgan/dw_morgan and run python manage.py migrate to run the migration and make sure the covid_observations table is created.
4) Uncomment out the app settings module dw_morgan.apps.DWMorganConfig in DWMorgan/dw_morgan/dw_morgan/settings.py to allow the test data to be loaded into the database.
5) Go back to DWMorgan/dw_morgan and run python manage.py runserver to start the app.





