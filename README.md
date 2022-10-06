# Calculatrice RPN
## Objectif
Réalisation d’une calculatrice RPN (notation polonaise inversée) en mode client/serveur

## Langages
- **Backend** : API REST, Python 3, Flask (préféré) ou Django.
- **Frontend** : Swagger 

## Setup (CMD)

### Create an environment

```
> py -3 -m venv venv
```
### Activate the environment

```
> venv\Scripts\activate
```

### Install requirements

```
> pip install -r requirements.txt
```

### Test

```
> nose2
```

### Run

```
> set FLASK_ENV="production"
> flask run --host=0.0.0.0 --port=8888
```


### Swagger

Ouvrez la [**documentation swagger**](http://localhost:8888) dans votre navigateur préféré 