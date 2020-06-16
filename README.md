# README - 2020_cropconnect

## Local testing
on Windows:
1. install Python (3.8.x)
2. open Powershell in project folder (where main.py is)
3. create virtualenv and activate it
4. run app from Powershell:
```
pip install requirements.txt
set FLASK-APP=main.py
flask run
```

## Multilanguage Support
Note: below commands should be executed in a terminal opened in the project root folder (i.e. where main.py is)

Using flask-babel: First get all the strings that need to be translated (marked using _() in templates and python code)
```
pybabel extract -F babel.cfg -k _l -o messages.pot .
```
this file "messages.pot" does not need to be included in the repo! It is just an intermediate result

Now generate translations for each supported language (de, it, fr)

/!\ this command overwrites your old translations! I.e. make sure you have saved them elsewhere if you want to reuse.
```
pybabel init -i messages.pot -d app/translations -l de
pybabel init -i messages.pot -d app/translations -l fr
pybabel init -i messages.pot -d app/translations -l it
```
once you made the translations, compile to usable files:
```
pybabel compile -d app/translations compiling catalog app/translations/de/LC_MESSAGES/messages.po to app/translations/de/LC_MESSAGES/messages.mo

pybabel compile -d app/translations compiling catalog app/translations/it/LC_MESSAGES/messages.po to app/translations/it/LC_MESSAGES/messages.mo

pybabel compile -d app/translations compiling catalog app/translations/fr/LC_MESSAGES/messages.po to app/translations/fr/LC_MESSAGES/messages.mo
```

## Deployment
Description on how to deploy the app goes here...

## Who do I talk to?
- Martin Baldinger (development) (martin.baldinger[@]gmail.com)
- Nicolas Peslerbe (deployment) (nicolas[@]peslerbe.com)
- Maxime Marchionno (maxime.marchionno[@]protonmail.com)
