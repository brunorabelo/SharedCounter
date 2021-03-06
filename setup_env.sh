#!/bin/sh

# shellcheck disable=SC2129
echo DEBUG=0 >>.env
echo DJANGO_SETTINGS_MODULE=appcounter.settings.production >>.env
echo PROD=1 >>.env

echo SQL_ENGINE=$SQL_ENGINE >>.env
echo DATABASE=$DATABASE >>.env
echo SECRET_KEY=$SECRET_KEY >>.env
echo DJANGO_ALLOWED_HOSTS=$DJANGO_ALLOWED_HOSTS >>.env
echo SQL_DATABASE=$SQL_DATABASE >>.env
echo SQL_USER=$SQL_USER >>.env
echo SQL_PASSWORD=$SQL_PASSWORD >>.env
echo SQL_HOST=$SQL_HOST >>.env
echo SQL_PORT=$SQL_PORT >>.env
echo REDIS_HOST=$REDIS_HOST >>.env
echo REDIS_PORT=$REDIS_PORT >>.env
echo WEB_IMAGE=$IMAGE:web >>.env
echo NGINX_IMAGE=$IMAGE:nginx >>.env
echo CI_REGISTRY_USER=$CI_REGISTRY_USER >>.env
echo CI_JOB_TOKEN=$CI_JOB_TOKEN >>.env
echo CI_REGISTRY=$CI_REGISTRY >>.env
echo IMAGE=$CI_REGISTRY/$CI_PROJECT_NAMESPACE/$CI_PROJECT_NAME >>.env
echo COMMIT_WEB_IMAGE_TAG=$IMAGE/web:$CI_COMMIT_SHA >>.env
echo COMMIT_NGINX_IMAGE_TAG=$IMAGE/nginx:$CI_COMMIT_SHA >>.env
echo SERVER_IP=$SERVER_IP >>.env
echo SERVER_USER=$SERVER_USER >>.env

echo POSTGRES_USER=$POSTGRES_USER >>.env.db
echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD >>.env.db
echo POSTGRES_DB=$POSTGRES_DB >>.env.db
