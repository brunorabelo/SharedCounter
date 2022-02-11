#!/bin/sh

ssh -o StrictHostKeyChecking=no $SERVER_USER@$SERVER_IP << 'ENDSSH'
  cd /home/ubuntu/app
  export $(cat .env | xargs)
  docker login -u $CI_REGISTRY_USER -p $CI_JOB_TOKEN $CI_REGISTRY
  echo $IMAGE
  echo $CI_REGISTRY
  echo $COMMIT_WEB_IMAGE_TAG
  docker pull $COMMIT_WEB_IMAGE_TAG
  docker pull $COMMIT_NGINX_IMAGE_TAG
  docker pull $IMAGE/web:$CI_COMMIT_REF_NAME
  docker pull $IMAGE/nginx:$CI_COMMIT_REF_NAME

  docker-compose -f docker-compose.prod.yml down
  docker-compose -f docker-compose.prod.yml build
  docker-compose -f docker-compose.prod.yml up -d
ENDSSH