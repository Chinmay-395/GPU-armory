# GPU-armory
A django+reactjs app that crawls on website to fetch Graphics-Card information

To setup 
1) clone the repo to local machine
2) create & activate virutal environment
3) run --> pip install -r requirements.txt
4) cd gpu_bot
# Note: migrations already exist thereby no need to run them again
5) Need to create a superuser
  5.1) run --> python manage.py createsuperuser
  5.2) fill in the credentials ie email,username,password
# to add all the tuples inside the csv into the sql-DB whichever you may choose [my preference--> PostgresSQl]
  a)  run --> python manage.py shell 
  b) run all the instructions inside loaddata.py
  c) it will push all the tuples into the django-admin as well as database
