[![Build Status](https://travis-ci.org/ngelrojas/cotizate-v2.svg?branch=master)](https://travis-ci.org/ngelrojas/cotizate-v2)
# COTIZATE V2

the project is a back end for cms crowfounding, is build in django, django rest framework, django rest framework jwt, postgresql,
celery rabbitmq and docker.

this configuration is based in multi-stage build, you can see the final image size is lighter.

it's integrated with swagger to documentation API's

is based in 12 factor to good developing

### Configuration env files and description

-   remove prefix ".example" in all .env files
-   `.env` file is develop environment
-   `.env_prod` is production environment
-   `.env.prod.db` is database production environment
-   `.env.prod.pgadmin` is pg-admin panel production
-   `.env.prod.rabbitmq` is to credential rabbitmq and the panel

in all .env put your data, to connection postgresql

#### run mode development in the file below

-   [doc to development](https://github.com/ngelrojas/cotizate-v2/blob/master/DEVELOPMENT.md)

#### run mode production in the file below

-   [doc to production](https://github.com/ngelrojas/cotizate-v2/blob/master/PRODUCTION.md)

#### use cotizate.supervisor
- copy and change name using mv cotizate.supervisor in etc/supervisor/conf.d/cotizateback.conf
- and using the command below
- supervisorctl reread
- supervisorctl update
- supervisorctl
- supervisor> start cotizateback # start service
- supervisor> tail cotizateback stderr # check errors 
