# nostr keyring app
===

This is currently a proof of concept application. Currently, it supports only one relay that is hardcoded. It does allow for the creation of brands and publishing both posts (short text notes) and blogs (lonform content notes).

## problem statement

Currently, one must crudely manage multiple keys with a nos2x extension in order to run multiple nostr accounts. Twitter and other social media giants allow for switching between brands easily once logged in.

## solution statement

One can create multiple brands, safely generate keypairs and handle publishing of events locally for marketing purposes.

## build
===

Create a virtual env by running. python3 -m venv env Then activate the virtual env. source env/bin/activate Once you have activated the virtual environment, run the following installs.

```
pip3 install -U pip
pip3 install -U setuptools
pip3 install -r requirements.txt
```

Now that you have activated the virtual env and installed the dependencies, type `cd mysite` in your terminal.
- Run `python3 manage.py makemigrations` 
- Run `python3 manage.py migrate`

### to use
- Run `python3 manage.py runserver` and now your webserver is running locally.
- Go to https://localhost:8000 to use!
- Create one or more Brands
- Create a Post or Blog!


## next steps
===

- Add support for NIP-3 and NIP-39 for brands concept. 