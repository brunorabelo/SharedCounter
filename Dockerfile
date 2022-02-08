FROM python:3.9-slim

WORKDIR /usr/src/app/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /docker/bin/entrypoint.sh ./docker/bin/
RUN sed -i 's/\r$//g' /usr/src/app/docker/bin/entrypoint.sh
RUN chmod +x /usr/src/app/docker/bin/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/app/docker/bin/entrypoint.sh"]


