from flask import Blueprint, request, Response
from apps.recyclops.models import locations
from DAO.database import db
import json
import csv


""""
Views file: 

module handles all functionality associated 
with the blueprint. Where a blueprint 
is simply a part of the app that 
is responsible for certain tasks/functionality. 
It is essentially a method to scale apps as 
they grow more complex. All blueprint endpoints 
are exposed here. 
"""

recyclopsApp = Blueprint("recyclopsApp", __name__)


"""
base route to serve HTML, CSS, JS, etc .... 
Subject to change if frontend wants 
to serve up static files from different 
server and call API indirectly 
"""
@recyclopsApp.route("/")
def root():
    pass


""" 
HTTP GET request to return list 
of recycling centers for a given 
material. 
"""
@recyclopsApp.get("/getLocations")
def getLocations():
    queryParams = request.args.to_dict()

    if "material" not in queryParams.keys():
        return Response(json.dumps(constructError("Query param 'material' was not provided", 400)),
                        status=400,
                        mimetype="application/json")

    try:
        filtered = {"locations": []}

        # - perform the database query. Please search for 'sqlalchemy queries' for more info
        # - on how the queries operate.
        #recyclingCenters = db.session.query(centers.center_name, centers.latitude, centers.longitude)\
        #    .filter(centers.material == queryParams["material"]).all()
        
        # STILL FIGURING OUT SPECIFICS FOR THIS
        # basically just want to query material from centers.csv for the respective company names, then for each company, query the center name from locations.csv to get the latitude and longitude
        recyclingCenters = db.session.query(centers).filter(centers.mat == queryParams['material']).all()
        recyclingCenters = []
        for rc in recyclingCenters:
            #filtered["locations"].append({"center name": rc[0], "latitude": rc[1], "longitude": rc[2]})
            location = db.session.query(locations).filter(locations.name == rc[2]).all()
            filtered['locations'].append({'center name': location[0], "latitude": location[1], "longitude": location[2]})
        return Response(json.dumps(filtered),
                        status=200,
                        mimetype="application=/json")

    except Exception:
        """ write better error handling functionality """
        return Response(json.dumps(constructError("Exception occurred during processing", 500)),
                        status=500,
                        mimetype="application/json")


""" 
HTTP post request to insert data into the 
'centers' table. This will be used to insert 
all database data when recycling center compilation 
is complete
"""
@recyclopsApp.post("/insertLocationsTable")
def createLocations():
    with open("locations.csv") as f:
        reader = csv.reader(f)

        for line in reader:
            db.session.add(locations(line[0], float(line[1]), float(line[2])))
        db.session.commit()

    return Response(json.dumps({"message": "Insertions successful!"}), status=200, mimetype="application/json")

def constructError(errorMsg, errorCode):
    return {"Error Message": errorMsg, "error code": errorCode}

@recyclopsApp.post("/insertCentersTable")
def createCenters():
    with open("centers.csv") as f:
        reader = csv.reader(f)

        for line in reader:
            db.session.add(centers(int(line[0]), line[1], line[2])
        db.session.commit()
"""
helper method to construct error messages
"""
def constructError(errorMsg, errorCode):
    return {"Error Message":  errorMsg, "error code": errorCode}
