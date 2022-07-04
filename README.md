**Hi!**


# **Step-by-step description of project deployment and launch**

   1. Clone project team -
`git clone - https://github.com/IvSDF/doc_list`

   2. Activate the virtual environment with a command -
`"source venv/bin/activate" (for Windows "venv\Scripts\activate" without a word source)`

   3. Set in the root folder install virtual environment -
`python -m venv venv`

   4. Activate the virtual environment with a command - 
`source venv/bin/activate`

   5. Install the necessary packages -
`pip install -r requirements.txt`

_______________________________________________________________________________
   6. # **_MySQL Database recovery_**

    1. Create an empty db -

1. mysql –u root –p
2. mypassword
3. CREATE DATABASE doc_list_db;
4. quit



    2. Restore the dump to the newly created database - 

1. mysql -u root -p -f doc_list_db < /home/username/dump_doc_list_db.sql
   mypassword
_________________________________________________________________________________

   7. Configure access to settings.py - 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'doc_list_db',
        'USER': [~~['root']~~](enter your username),
        'PASSWORD': ['~~PASSWORD~~'](enter the password),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

   8. Сreate a superuser
`python manage.py createsuperuser`
or use:
    Username: admin
    Password: admin



# **API Documentation**

    1. Use - http://127.0.0.1:8000/swagger/ (This is not a complete api documentation. 
                                                Here you will find the main requests GET)

        return All direction - 
            GET /api/v1/direction
        return All doctors - 
            GET /api/v1/doctors  (WITH PAGINATION - "2")
        return ITEM doctor - GET 
            GET /api/v1/doctors/(slug) 

    2. Filters - 
    "filtering doctor by direction"
        GET /api/v1/doctors/?directions="title"
    "filtering doctor by years of experience"
        GET /api/v1/doctors/?directions=&years_of_experience_min=<int>&years_of_experience_max=<int>

    3. Ordering - 
    "years of experience"
        GET /api/v1/doctors/?ordering=years_of_experience
        GET /api/v1/doctors/?ordering=-years_of_experience

    "birthday"
        GET /api/v1/doctors/?ordering=birthday
        GET /api/v1/doctors/?ordering=-birthday
