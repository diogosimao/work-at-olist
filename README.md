# NEATtree (Nested explicit atomic test) tree

This is in order to take part into [Work at Olist](https://github.com/olist/work-at-olist).

For original `README.md` [see here](https://github.com/diogosimao/work-at-olist/blob/8df996261784661a5a54d0fdf9671b7c5f7cf2e2/README.md).

## Stack

- Python >= 3.5
- PIP
- Pipenv

## Project Requirements

- Django >= 1.10
- django-environ
- django-generate-secret-key
- django-mptt
- djangorestframework
- djangorestframework-recursive
- psycopg2
- gunicorn
- whitenoise

## Run the app locally

1. Make sure you have [Python >= 3.5](https://www.python.org/downloads/source/) and [PIP](https://pip.pypa.io/en/stable/installing/) installed.

    1.1. In order to install it on Ubuntu like systems run:

        $ sudo apt-get install python3 \
            sudo apt-get install python3-pip

2. Install `Pipenv`.

        $ sudo pip3 install pipenv

3. Git clone this [repo](https://github.com/diogosimao/work-at-olist). Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed

        $ git clone https://github.com/diogosimao/work-at-olist.git && cd work-at-olist

4. Use `Pipenv` to create a virtualenv, install its dependencies and activate the virtualenv.

        $ pipenv --three && pipenv install && pipenv shell

5. Make sure you have [PostgreSQL](https://www.postgresql.org/download/) installed running on port 5432

6. Set your local user and password to `./bin/start_development.sh` and create the database

        $ createdb neattree

7. Run `./bin/start_development.sh`

Development server should be up at [http://localhost:8000/](http://127.0.0.1:8000/).


## Deploy the app to [Heroku](https://www.heroku.com/)

1. Make sure you have [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed and that you are logged in

2. Set `DEBUG=False` for safety measure

        $ heroku config:set DEBUG=False

3. Be aware that [Release Phase](https://devcenter.heroku.com/articles/release-phase#defining-a-release-command) will be executed as you deploy it.

    3.1. It will generate a Django *production* environment `SECRET_KEY`

    3.2. It will run *Django makemigrations*

    3.3. It will run *Django migrate*

4. Deploy it, [see here](https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app)

5. Get you herokuapp.com url and access it on your browser.

        $ heroku info -s | grep web_url | cut -d= -f2
