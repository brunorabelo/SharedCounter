# AppCounter
AppCounter

Initial steps: 

sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
## Banco de dados
sudo -u postgres psql

CREATE DATABASE appcounter;

CREATE USER appcounter WITH PASSWORD 'appcounter';
ALTER ROLE appcounter SET client_encoding TO 'utf8';
ALTER ROLE appcounter SET default_transaction_isolation TO 'read committed';
ALTER ROLE appcounter SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE appcounter to appcounter;

\q