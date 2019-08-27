# Homepage
## 安装
```bash
# 初始化虚拟环境(Python3)
pipenv --three
pipenv shell
# 安装依赖
pipenv sync
python manage.py migrate
```
## 部署
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