# PythonWADec23 - Django Htmx Tailwind Alpine

## A presentation to the PythonWA meetup group with some demonstrations.

### Creating the database

This demo uses the postgres database for the active search demo. Ensure that you have docker installed by following the instructions 
here [Install Docker Engine](https://docs.docker.com/engine/install/)

Then start a postgres container with the following command:

`docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=password postgres`

Now we are going to create a database in teh postgres container. Open up a terminal in the container with the following
command in a new terminal window:

`docker exec -it postgres bash`

Now connect to postgres using psql with the following command:

`psql -h localhost -U postgres`

We can now create a database for django to use:

`CREATE DATABASE django;`

To verify that the database was created successfully, we can check for the database 'django' with the following command:

`\l`

### Installing the project dependencies

Next, lets set up a virtual environment and install the project dependencies. Run the following commands from the 
project root folder:

`python3 -m venv venv`

Now we can activate the virtual environment with:

`source venv/bin/acitvate`

Then install the dependencies:

`pip install -r requirements_dev.txt`

### Migrating the database, creating a user and adding some blog posts

We can now use django to create the tables by migrating:

`./manage.py makemigrations`

followed by:

`./manage.py migrate`

Now we can create a superuser with your own credentials:

`./manage.py createsuperuser`

Lets also add some dummy blog posts:

`./manage.py create_app_data`

### Installing the tailwind CSS dependencies

Now to make sure that any changes we make to our layout are updated by tailwind, install the dependencies:

`manage.py tailwind install`

*Note:* This project has the tailwind app preinstalled, if you want to use tailwind in your own project, follow the
installation steps [here](https://django-tailwind.readthedocs.io/en/latest/installation.html).

### Running the servers

In order for tailwind to add any changes to our css file, we need to have a running tailwind server:

`./manage.py tailwind start`

Finally, run the django server with:

`./manage.py runserver`

### Useful Docs

[Django-Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html)

[Tailwind CSS](https://tailwindcss.com/)

[Django-HTMX](https://django-htmx.readthedocs.io/en/latest/installation.html)

[HTMX](https://htmx.org/)

[AlpineJS](https://alpinejs.dev/)

[PinesUI](https://devdojo.com/pines)

Built with [Django Cookiecutter](https://github.com/imAsparky/django-cookiecutter)
