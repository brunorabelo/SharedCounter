#!/bin/sh

# shellcheck disable=SC2129
echo DEBUG=0 >> /docker/config/.env.prod

echo SQL_ENGINE=$SQL_ENGINE>> /docker/config/.env.prod
echo DATABASE=$DATABASE >> /docker/config/.env.prod
echo SECRET_KEY=$SECRET_KEY >> /docker/config/.env.prod
echo DJANGO_ALLOWED_HOSTS=$SECRET_KEY >> /docker/config/.env.prod
echo SQL_DATABASE=$SQL_DATABASE >> /docker/config/.env.prod
echo SQL_USER=$SQL_USER >> /docker/config/.env.prod
echo SQL_PASSWORD=$SQL_PASSWORD >> /docker/config/.env.prod
echo SQL_HOST=$SQL_HOST >> /docker/config/.env.prod
echo SQL_PORT=$SQL_PORT >> /docker/config/.env.prod
echo REDIS_HOST=$REDIS_HOST >> /docker/config/.env.prod
echo REDIS_PORT=$REDIS_PORT >> /docker/config/.env.prod
echo WEB_IMAGE=$IMAGE:web  >> /docker/config/.env.prod
echo NGINX_IMAGE=$IMAGE:nginx  >> /docker/config/.env.prod
echo CI_REGISTRY_USER=$CI_REGISTRY_USER   >> /docker/config/.env.prod
echo CI_JOB_TOKEN=$CI_JOB_TOKEN  >> /docker/config/.env.prod
echo CI_REGISTRY=$CI_REGISTRY  >> /docker/config/.env.prod
echo IMAGE=$CI_REGISTRY/$CI_PROJECT_NAMESPACE/$CI_PROJECT_NAME >> /docker/config/.env.prod
echo SERVER_IP=$SERVER_IP >> /docker/config/.env.prod
echo SERVER_USER=$SERVER_USER >> /docker/config/.env.prod


