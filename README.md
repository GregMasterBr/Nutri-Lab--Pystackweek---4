# Construct 

Sistema de Gerenciamento de Construção

## Como desenvolver?
1. Clone o repositório
2. Crie um virtualenv com a versão mais recente do python (3.10)
3. Ative o virtualenv
4. Configure a instância com o .env
5. Execute os testes

```console
git clone https://github.com/GregMasterBr/Construct.git Construct
cd Construct
python -m venv venv
venv/Scripts/Activate.ps1
pip install -r requirements.txt ou pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?
1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina o DEBUG=False
5. Configure o serviço de e-mail (ex: Sendgrid)
6. Envie o código para o heroku


```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#Configurar o e-mail
git push heroku master --force

```

Projeto hospedado no Heroku  
<https://##>
