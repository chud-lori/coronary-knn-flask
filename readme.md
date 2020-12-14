# Heart Disease Predictor using KNN Algorithm and Flask Micro Web Framework

Nothing.
Prediction Heart Disease

## Requirements

- Python 3.6
- IDE (I use VScode)

## Set Up

- Create an virtual enviroment and make sure to run inside it
- Run `pip install -r requirements.txt`
- Set the `config.py` for the database and etc.
- Create a database named `corpe`
- Place `heart.csv` inside `instance` directory or create the directory if not exist
- In python interpreter run

```python
    from corpe import db, create_app
    db.create_all(app=create_app())
```

- Create `config.py` file

```python
class Config(object):
    SECRET_KEY = # generate random key using: os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@database' # connect to database system

```

## Set Up environment variables (Linux)

Set up environment variable from root project directory
Set for development mode

```bash
export FLASK_ENV=development
export FLASK_APP=setup.py
```

## Run

Run this command and access the web app at `localhost:5000`

```bash
flask run
```

Access `localhost:5000/gen` to seed admin\
Access `localhost:5000/gen-ds` to seed datasets

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
