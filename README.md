# Teste Técnico Desenvolvedor(a) Python Júnior [REMOTO]

## Instalação

Faça o clone do repositório
 
`$ heroku git:clone -a instruct-teste-app`

`$ cd instruct-teste-app`

`$ python manage.py migrate`

`$ python manage.py collectstatic` 

## Executando a aplicação

`$ python manage.py runserver`

## Executar teste

Com a aplicação rodando, execute o teste com o k6

`$ k6 run -e API_BASE='http://localhost:8000/' tests-open.js`
