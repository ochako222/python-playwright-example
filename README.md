# Initialization python project

First of all, we need to update our global python files 

```bash
brew update
brew install pyenv
brew install python

brew info python
```

Now we need to activate a virtual environment
```bash
python3 -m venv env
source env/bin/activate.fish
```

In case to deactivate python environment, type:

```bash
deactivate
```

Now we have the project structure and we can install the first libraries
```bash
echo -e "requests\npytest" > requirements.txt
pip install -r requirements.txt
```
We installed `request` inside the Python virtual environment

This project use playwright, when you launch tests first time, don't forget to launch installation first:

```bash
playwright install
```

Now to launch existed tests we can run command:

```bash
python -m pytest
```

or use existed `Makefile` script:

```bash
make single
```

## Create .env file
```bash
PORTAL_URL=
USER_NAME=
USER_PASSWORD=
```