#!/bin/sh

ssh -o StrictHostKeyChecking=no $SERVER_USER@$SERVER_IP << 'ENDSSH'
  cd /home/ubuntu/app
  export $(cat .env | xargs)
  docker login -u $CI_REGISTRY_USER -p $CI_JOB_TOKEN $CI_REGISTRY
  docker pull $TAG_COMMIT
  docker container rm -f appcounter || true
  docker run -d -p 8000:8000 -p 8001:8001 -v static_volume:/home/app/web/staticfiles --env-file=.env --name appcounter $TAG_COMMIT
ENDSSH