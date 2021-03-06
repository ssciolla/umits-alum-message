## UM ITS Job Application Project
## alum_message application

### Description

This project was created as part of the application process for a full-time position in the Teaching and Learning group at University of Michigan Information and Technology Services.

 The alum_message application aims to help to connect University of Michigan alumni by making it simple to direct message one alum or multiple alumni using only uniqnames.</p>

### Notes on database setup

This application uses an SQLite database, `alum_message.db`, as its backend. The database is included in this repository and can be found in the `alum_message` directory. The Python script used to create the database schema is included in the `database_setup` directory.

### Setup instructions

1. Clone the repository.

```
git clone https://github.com/ssciolla/umits-alum-message.git
```

2. Create a virtual environment.

```
cd umits-alum-message/alum_message
virtualenv venv
source venv/Scripts/activate #(for Unix/Bash)
venv\Scripts\activate` #(for Command Prompt on Windows)
```

3. Install the dependencies.

```
pip install Django
pip install django-crispy-forms
pip install django-filter
```

4. Set up a secret key.

- Generate a secret key (the [Djecrety Web tool](https://djecrety.ir/) seems like a simple way to do this).
- Create a new `secrets.py` file in the `umits-alum-message/alum_message/mysite directory.`
- Add the following line to `secrets.py`:

```
secret_key = '[Your new secret key goes here]'
```

5. Start up the server.

```
python manage.py runserver
```

6. View the application at localhost:8000.

Note: A Django superuser has been created for reviewers' use in accessing the admin site at localhost:8000/admin. The login details are the following:

- Username: project_superuser
- Email: ssciolla@umich.edu
- Password: um_its_719

### Resource Links and Acknowledgments

The following resources were referenced while creating this application:

- [Django documentation](https://docs.djangoproject.com/en/2.2/)
- [SQLite documentation](https://www.sqlite.org/docs.html)
- [django-filter documentation](https://django-filter.readthedocs.io/en/master/index.html)
- [arwhyte/SI664-docs repository](https://github.com/arwhyte/SI664-docs)

 I would like to acknowledge my indebtedness to my former instructor, Anthony Whyte, who provided extensive guidance, resources, and starter code during Fall 2018 as part of UMSI 664: Database Application Design. In particular, his assignments and documentation supplied jumping off points for using Bootstrap/CSS, django_filters, and crispy_forms. The resources he created are available in a public repository (see above).
 
 Sample instances of alumni and messages were inspired by the original *Star Wars* trilogy.