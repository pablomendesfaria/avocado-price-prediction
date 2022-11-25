# Previsão de Preço do Abacate Hass

Módelo de ML que realiza a previsão do preço do abacate.

## Dev.:

1. Create virtual env with [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html):

```
$ mkvirtualenv avocado -p python3
```

2. Activate virtual env:

```
$ workon avocado
```

3. If you want to deactivate:

```
$ deactivate
```

4. Install requirements:

```
$ pip install -r requirements.txt
```

And then...

```
$ pip install -e .
```

### To run the app and make predictions

Be at the root of the project, and do:

```
$ streamlit run dash.py
```

You can access the application in the browser by the URL: http://localhost:8501

To stop the application:

```
$ Ctrl + c
```