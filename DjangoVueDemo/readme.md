# 1 Demo Components
- Backend: Django + DRF
- Frontend: Vue.js
- DB: MySQL `TODO`
- Cache: Redis `TODO`
- Web Server: uwsgi
- Process Control: supervisor
- Load Balancer, Web Server, & Reverse Proxy: nginx 

# 2 Backend mysite
## 2.1 [install django](https://www.djangoproject.com/)
pip3 install django

## 2.2 create django project
python -m django startproject mysite

## 2.3 create django app
python3 manage.py startapp app1

## 2.4 run server
python3 manage.py runserver 8008

## 2.5 alter mysite/settings.py
add app1  
add corsheaders

## 2.6 add views/urls
app1/views  
mysite/urls

# 3 Frontend mysitevue
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

## 3.6 run service
npm run dev

## 3.7 wrap service
npm run build

## 3.8 add router
testrein

# QA
## 1 check nvm installed versions
nvm list
## 2 switch nvm default version
nvm alias default 16.15.1
## 3 nvm uninstall specific version nodejs
nvm uninstall 16.15.1