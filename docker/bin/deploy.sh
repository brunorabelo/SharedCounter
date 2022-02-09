#!/bin/sh

ssh -o StrictHostKeyChecking=no $SERVER_USER@$SERVER_IP << 'ENDSSH'
  cd /home/ubuntu/app
  export $(cat .env | xargs)
  docker login -u $CI_REGISTRY_USER -p $CI_JOB_TOKEN $CI_REGISTRY
  docker pull $IMAGE:web
  docker pull $IMAGE:nginx
  docker-compose -f docker-compose.prod.yml up -d
ENDSSH