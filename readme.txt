'-------------------------------------------------------------------------------
'=- Tools  ****
'-------------------------------------------------------------------------------
1. Download visual studio code(v1.85.1)
   - https://code.visualstudio.com/

2. Download python(v3.10.4)
   - https://www.python.org/downloads/  

3. Download xampp
   - https://www.apachefriends.org/index.html

4. Install django
  - pip install django


'-------------------------------------------------------------------------------
'=- extensions VSCODE  ****
'-------------------------------------------------------------------------------


'-------------------------------------------------------------------------------
'=- extensions CHROME  ****
'-------------------------------------------------------------------------------

'-------------------------------------------------------------------------------
'=- Methods  ****
'-------------------------------------------------------------------------------
1. To create virtual environment (vscode)
   - python.exe -m venv <envName> eg:usepmscore

1.a To Install django 
   - pip install Django

2.a To activate vitrual environment (vscode)
   - <envName>\scripts\activate.bat

2.b To deactivate virtual environment (vscode)
   - deactivate

3. create new django project 
  - django-admin startproject <projectName> eg:usepDashAPI 

3.a create startapp 
  - python manage.py startapp <appName> eg mainApp

4. Create new django App
  - python .\manage.py startapp usepdashboard

5A. After creating model for database migrate the model
 - python.exe .\manage.py makemigrations <appName> eg. mainApp

5B. Then migrate to mysql Server
  - python .\manage.py migrate <appName> eg mainApp

6A. Created python admininstration backend
  - python manage.py migrate

6B. Create superuser account
  - python  manage.py createsuperuser 

7. To rearrage columns in MySql
  - ALTER TABLE <table_name> MODIFY <column> char(1) AFTER username 