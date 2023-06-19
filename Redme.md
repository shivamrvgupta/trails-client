Setup: 
  1. Install python
  2. open project in vs code
  3. create and activate the virtual env
  4. use cmd - pip install -r requirements.txt this will download all the required packages in the project
  5. after installing the packages migrate the database 
  6. cmd - python manage.py makemigrations
  7. then cmd - python manage.py migrate
  8. After migration create database superuser cm - python manage.py createsuperuser
  9. then good to go use your server cmd - python manage.py runserver
  10. for any urls check url.py in every app 

  basic urls for admin pannel :
    localhost:8000/admin
    localhost:8000/accounts/login
    localhost:8000/accounts/register
    localhost:8000

