# How to setup and run this app
### 1. Create dir (ex. `mkdir todoapp` ) for app and clone this repository.
### 2. Create and run python virtual environment.

   + `python -m venv ./venv`
   + `source ./venv/bin/activate`

### 3. Install app dependencies `pip install -r requirements.txt`
### 4. Inside app dir create new dir called *instance* `mkdir instance`
### 5. Inside instance dir create file called `config.py` and add following line
```python
SECRET_KEY = 'your_secret_key_goes_here'
```
### 6. Run flask with `flask run` command
### 7. App should now be working on address `http://localhost:5000/todos`