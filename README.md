# URLShort

Encurtador de URLs.

Link: http://urlshortme.herokuapp.com/

Admin: http://urlshortme.herokuapp.com/admin

Login: demo

Pass: urlshortme

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone https://github.com/klebercode/urlshort.git
cd urlshort
python -m venv .urlshort
source .urlshort/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para instância
4. Defina DEBUG=False
5. Envie o código para o heroku

```console
heroku create minhainstancia
# certifique-se de excluir a variável DATABASE_URL
heroku config:push
# rode o comando: python contrib/secret_gen.py
# e copie a SUA_KEY
heroku config:set SECRET_KEY=SUA_KEY
heroku config:set DEBUG=False
git push heroku master --force
```
