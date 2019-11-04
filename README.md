# Grandpy

## Objectif

Création d'une application qui permet de donner l'adresse d'un lieu et une petite description de ce dernier.
L'application utilse Flask et deux API : Google Maps et Wikipedia.

### Installation
1. Virtualenv & requirements
```
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```
2. Enter your API Key in the flask_gbapp/scripts/config.py file.

### Start

```
# run
python run.py

# test
python flask_gbapp/test_app.py
```
