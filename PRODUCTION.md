## PRODUCTION

#### Files .env to production

-   `.env_prod` is production environment
-   `.env.prod.db` is database production environment
-   `.env.prod.pgadmin` is pg-admin panel production
-   `.env.prod.rabbitmq` is to connect rabbitmq and celery

#### Change file celery.py to production

-   path: app/api/celery.py

```python
    from api.settings import production
```

```python
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings.production')
```

```python
    production.DEFAULT_FROM_EMAIL
```

#### Change file serializers.py to production, module USERS

-   path: app/users/serializers.py

```python
    from api.settings import production
```

```python
    URL_TO_SEND = production.URL_PRODUCTION
```

#### Change file manage.py to production

-   path: app/manage.py

```python
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings.production")
```

#### Run production

```python
    docker-compose -f docker-compose.prod.yml up -d --build
```

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py migrate
```

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py county_city
```

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py users
```

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py campaing_header_body
```

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py phases
```

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py rewards
```

```python
    docker-compose -f docker-compose.prod.yml exec api python manage.py comments
```
#### run server send email production using supervisor

-   give permissions to `server_email.sh` file:

```python
   chmod +x server_email.sh
```

-   install supervisor in your server
-   copy `cotizate.conf` file into the path supervisor:
-   path: etc/supervisor/conf.d
-   run this command:

```python
     sudo supervisorctl reread
```

```python
     sudo supervisorctl update
```

```python
     sudo supervisorctl status
```

```python
     sudo supervisorctl restart `cotizate_server`
```

#### Testing

-   Don't stop container
-   Run the testing

```python
 docker-compose -f docker-compose.prod.yml run api sh -c "python manage.py test && flake8"
```

#### troubleshooting

-   if the panel admin not working try this:

-   don't stop current container

-   edit docker-compose.prod.yml and add '/api/' in volumes like this:

```python
    static_volume: /home/app/api/api/staticfiles
```

-   save file docker-compose.prod.yml

-   run the script

```python
    docker-compose -f docker-compose.prod.yml run api sh -c "python manage.py collectstatic --no-input --clear"
```
