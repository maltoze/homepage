# Homepage
## Installation
```bash
$ git clone git@github.com:maltoze/homepage.git
$ cd homepage
$ pipenv install --dev
$ pipenv shell
$ python manage.py migrate
$ python manage.py runserver
```
## Deployment
### Heroku
``` bash
$ heroku login
$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku pg:promote DATABASE_URL
$ heroku config:set ENVIRONMENT=PRODUCTION
# Use GitHub
# App connected to GitHub -> Automatic deploys/Manual deploy
$ heroku run python manage.py createsuperuser
```