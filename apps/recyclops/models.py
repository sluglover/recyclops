from DAO.database import db
import sqlalchemy as sa


""" 
model classes used for database actions. 
A model class inherits from a sub-class 
of the instantiated database to declare 
it as a database model. Each class is used 
to represent a table within the database. 
It can be used to create a table, insert data into 
a table, and retrieve data from a table. 

The name of the class needs to match the name
of the table precisely if the table already 
exists. With that, all defined columns also 
need to be declared as class variables. 
"""
class centers(db.Model):
    material    = sa.Column(sa.String, primary_key=True)
    center_name = sa.Column(sa.String)
    latitude    = sa.Column(sa.FLOAT)
    longitude   = sa.Column(sa.FLOAT)


    def __init__(self, material, center_name,  latitude, longitude):
        self.material    = material
        self.center_name = center_name
        self.latitude    = latitude
        self.longitude   = longitude
