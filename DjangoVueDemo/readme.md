# 1 demo components
- backend: Django + DRF
- frontend: Vue.js
- DB: MySQL
- cache: Redis

# 2 backend
## 2.1 [install django](https://www.djangoproject.com/)
pip3 install django

## 2.2 create django project
python -m django startproject mysite

## 2.3 create django app
python3 manage.py startapp app1

## 2.4 alter mysite/settings.py

## 2.5 add views/urls

## 2.6 run server
python3 manage.py runserver

# 3 frontend
## 3.1 [install vue-cli](https://cli.vuejs.org/guide/installation.html)
npm install -g @vue/cli

## 3.2 check it
vue --version

## 3.3 install vue/cli-init
npm i -g @vue/cli-init

## 3.4 create project base on webpack
vue init webpack mysitevue

## 3.5 install vue router
npm i -save vue-router