Welbex Test Task

## PostgreSQL setup
after installation of PostgreSQL:

```shell
~$ sudo -u postgres psql
postgres=#
CREATE DATABASE welbex;
CREATE USER welbex_user WITH PASSWORD 'password';

ALTER ROLE welbex_user SET client_encoding TO 'utf8';
ALTER ROLE welbex_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE welbex_user SET timezone TO 'Europe/Moscow';

GRANT ALL PRIVILEGES ON DATABASE welbex TO welbex_user;
```

Inside Django project folder
```python
#welbex/settings.py
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'welbex',
        'USER': 'welbex_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
...
```

```shell
(venv) ~$ ./manage.py shell < tours/db_filler.py
(venv) ~$ ./manage.py makemigrations && ./manage.py migrate
(venv) ~$ ./manage.py runserver
```

## Result
![alt](https://drive.google.com/uc?export=view&id=1Y3XdiJk1uu_o494PPc902j-_ClAlue9o)

## Summary
1. Set PostgreSQL on local machine ✅
2. Created simple Django app and database filler ✅
3. AJAX (but I tried) ❌