# AppCounter 
 
You can test it at https://sharedcounter.pt

## Description

A realtime web application for counting things in a collaborative and real-time manner. Visitors, team accomplishment, events, stuff, whatever you want to count.

Technologies:
- Django
- Channels
- Redis
- Bulma
- Vue.JS
- Nginx
- docker
- docker-compose
- postgres

The application was deployed at AWS EC2 running in a docker-compose environment.
It is used a CI-CD pipeline to deploy the application and to test it.

## Extra:
There is also a mobile version built in React Native at https://github.com/guilevieiram/shared_count

## Run

Requirements:
- docker 
- docker-compose 

Run:

```
docker-compose -f docker/compose/docker-compose.yml up --build
```
