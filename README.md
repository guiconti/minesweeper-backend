## Minesweeper APIs ##

This repository contains APIs for the game Minesweeper. You can check out the front-end for this project by clicking [here](https://github.com/guiconti/minesweeper-frontend)

### Setup ###

Install packages
```pip install -r requirements.txt```

Apply database migrations

```python manage.py migrate```

Run the application
```python manage.py runserver```

### Tests ###

To run tests
```python manage.py test games```

To run tests and generate a coverage report
```coverage run --source='.' manage.py test games```

### Coverage ###
![Coverage](https://i.imgur.com/OMGYnjd.png)

### Docs ###

You can check the APIs documentantion [here](https://guiconti.github.io/minesweeper-backend/)