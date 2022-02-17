# Stage 1 - build frontend app
FROM node:10-alpine as build-deps

WORKDIR /app/

COPY frontend/package.json frontend/package-lock.json /app/
RUN npm install

COPY frontend /app/
#COPY .env /app/.env
RUN npm run build


# Stage 2 - nginx & frontend dist
FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY docker/nginx/nginx.conf /etc/nginx/conf.d
COPY --from=build-deps /app/dist/ /dist/

CMD ["nginx", "-g", "daemon off;"]
