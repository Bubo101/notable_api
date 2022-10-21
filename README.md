Hello Notable Staff!

INSTALLATION & USE: 
-Fork and clone from git
-Get into project directory
-Open in VS code or other editor 
-Activate virtual environment:
    `source .venv/bin/activate`
-All dependencies should be installed (so skip this unless need3ed) but if django is not working:
    `pip install django`
-Run `python manage.py makemigrations`
-Run `python manage.py migrate` (this sest up the database)
-Run `python manage.py createsuperuser`
-Run `python manage.py runserver`
(suggest something like user:staff, pass:staff, can hit enter to skip the email entry and select "y" to confirm password even though it is a simple passord)

-In a browser, travel to localhost:8000/admin/ and use your credentials
-Add one or two doctor instances (and appointments if you'd like)

-Make API calls through the browser or a service like insomnia, postman.

-Example Calls:
    -New Appoitment(POST):
        `localhost:8000/api/appointments/new/`
        With JSON body:
        {
			"first_name": "Cathys",
			"last_name": "Stricklands",
			"date_time": "2022-10-24T11:45",
			"kind": "Yearly Checkup",
			"doctor": "Jones"
        }
    -Appointments filtering by Doctor(id) and Date(MMDDYYYY) (GET):
        `localhost:8000/api/appointments/1/10242022`. (doctor id first, then date in MMDDYYYY format)

    -List All Providers (GET):
        `localhost:8000/api/providers/`

    -Delete Appointment(DEL):
        `localhost:8000/api/appointments/delete/3/` (by appt id)


