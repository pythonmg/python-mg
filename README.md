Python-MG
=========

Nova versão do site da comunidade Python de Minas Gerais.


Primeiros passos
-------------
Faça o clone do código
   
   `git clone https://github.com/python-mg/python-mg.git`

Vá para a pasta do projeto e instale as libs necessárias
   
   `pip install -r requirements`


Estamos utilizando o MySQL e definimos o banco de dados por variaveis de ambiente.
Precisamos de 3 variaveis para as configurações do DB, "DB_NAME_PYMG", "DB_USER_PYMG", "DB_PASS_PYMG".
 
 * **DB_NAME_PYMG** é o nome do banco de dados para o projeto.
 * **DB_USER_PYMG** é o nome do usuário que possui acesso ao banco de dados.
 * **DB_PASS_PYMG** é a senha de acesso ao banco de dados.

Exemplo de configuração:
   

      export DB_NAME_PYMG=pymg
      export DB_USER_PYMG=mysql_user
      export DB_PASS_PYMG=mysql_pass


Agora já pode rodar o syncdb para criar as tabelas no banco de dados.
   
   `python manage.py syncdb`

Carregue os arquivos estáticos
   
   `python manage.py collectstatic`

Rode o server
   
   `python manage.py runserver`
   
Abra seu navegador e acesse http://127.0.0.1:8000


Wiki
------
https://github.com/python-mg/python-mg/wiki/

Como contribuir
----------------
https://github.com/python-mg/python-mg/wiki/Como-contribuir

Padrões utilizados
---------------
https://github.com/python-mg/python-mg/wiki/Padr%C3%B5es-utilizados


Encontros
-------------

*Encontro dia 16/11* 
- Objetivo:
    * Ajustes no site
    * Definir detalhes de layout
    * Compra de dominio do site
    * Debate sobre hospedagem
- Participantes: 
    * Igor dos Santos http://github.com/igr-santos
    * Lucas Magnum http://github.com/lucasmagnum
    * Neilson Lima http://github.com/Neilson
    * Paulo Rodrigues Gomes prxgomes@gmail.com
    * Saint Clair de Sousa http://github.com/saintclair
    * Paulo Roberto http://github.com/mauler

*Encontro dia 02/11* 
- Objetivo:
    * Definir o foco do novo site
    * Configurar e organizar o ambiente para o desenvolvimento do novo site
    * Determinar próximas etapas
- Participantes: 
    * Fernando Oliveira http://github.com/fernandopso
    * Igor dos Santos http://github.com/igr-santos
    * Lucas Magnum http://github.com/lucasmagnum
    * Neilson Lima http://github.com/Neilson
    * Paulo Rodrigues Gomes prxgomes@gmail.com
    * Saint Clair de Sousa http://github.com/saintclair
