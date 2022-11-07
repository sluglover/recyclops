from flask_sqlalchemy import SQLAlchemy


""""
Database instantiation file: 

We'll use a very simplistic database framework 
known as flask_sqlalchemy. To connect to a 
database it solely requires the connection 
URI. It then has to register with the 
flask app for database management. The 
db object can be imported anywhere within 
the project and can be used as desired

"""
db = SQLAlchemy()


"""" 
app - flask app to register 
username - username of the database
password - password associated with 'username' 
database - name of the database to connect to
"""
def db_init(app, username, password, database):
    """todo: replace as fstring"""
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql://{username}:{password}@localhost/{database}"
    db.init_app(app)
