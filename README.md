Python-MG
=========

Nova versão do site da comunidade Python de Minas Gerais.

[![Build Status](https://travis-ci.org/python-mg/python-mg.svg?branch=master)](https://travis-ci.org/python-mg/python-mg)


Primeiros passos
-------------
Faça o clone do código

   `git clone https://github.com/python-mg/python-mg.git`

Vá para a pasta do projeto e instale as libs necessárias

   `pip install -r requirements.txt`


Agora já pode rodar o syncdb para criar as tabelas no banco de dados.

   `python manage.py syncdb`

Rode o server

   `python manage.py runserver`

Abra seu navegador e acesse http://127.0.0.1:8000

Rode os testes
-------------

`./manage.py syncdb --settings=pymg.settings.test`

`./manage.py migrate --all --settings=pymg.settings.test`

`./manage.py test --settings=pymg.settings.test`


Atualiza elementos do site
-----

Feeds - Importe os feeds

`./manage.py loaddata data/feeds.json`

`./manage.py update_feeds`


Twitter - Importe as hashtags e os usuarios

`./manage.py loaddata data/twitter.json`

`./manage.py import_tweets`


Meetup - Importe os membros

- Configure chave-api e url grupo no settings

```
MEETUP_API_KEY={key_developer}
MEETUP_GROUP_URLNAME{url_name_group}
```

`./manage.py update_members`


Veja a pagina inicial.


Wiki
------
https://github.com/python-mg/python-mg/wiki/

Como contribuir
----------------
https://github.com/python-mg/python-mg/wiki/Como-contribuir

Padrões utilizados
---------------
https://github.com/python-mg/python-mg/wiki/Padr%C3%B5es-utilizados
