# Doctor API
Doctorapi for managing doctors and their specializations

## List of API endpoints:
- http://127.0.0.1:8000/api/doc/swagger/ - use this endpoint for convenient managing of all existing api endpoints
- http://127.0.0.1:8000/admin/ - admin panel
- http://127.0.0.1:8000/api/doctor/areas/ - list of areas (specializations)
- http://127.0.0.1:8000/api/doctor/doctors/ - list of doctors
- http://127.0.0.1:8000/api/doctor/doctors/?areas= - filter by area id (ex. ?areas=2,5)
- http://127.0.0.1:8000/api/doctor/doctors/?experience - filter by doctor experience (ex. ?experience=2)
- http://127.0.0.1:8000/api/doctor/doctors/{slug}/ - doctor detailed endpoint (use value of slug field from Doctor model)

## How to run:
To run the application you have two variants:

FIRST:
1. git clone
2. run command `pip install -r requirements.txt`
3. run command `python manage.py createsuperuser` and create superuser for using admin panel
4. run command `python manage.py runserver`
5. visit url http://127.0.0.1:8000/admin/ and create areas, doctors and check all endpoints that listed above
6. you have to have mySQL installed on you computer

SECOND:
1. git clone
2. run command `docker-compose up --build` (docker app has to be installed on your computer)
