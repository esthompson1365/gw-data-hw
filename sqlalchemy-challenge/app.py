import numpy as np
import pandas as pd

import datetime as dt
from datetime import timedelta

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def prcp():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all precipitation records
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_precipitation
    all_precipitation = []
    for date, prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        all_precipitation.append(precipitation_dict)

    return jsonify(all_precipitation)

@app.route("/api/v1.0/stations")
def stations():

    session = Session(engine)



    results = session.query(Station.name).all()

    session.close()


    all_stations = []
    for name in results:
        stations_dict = {}
        stations_dict["name"] = name
        all_stations.append(stations_dict)

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def temps():

    session = Session(engine)

    last_year = dt.datetime(2017, 8, 23) - timedelta(365)

    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date > last_year).all()
   
    session.close()

    lastyr_temps = []
    for date, tobs in results:
        temps_dict = {}
        temps_dict["date"] = date
        temps_dict["temp"] = tobs
        lastyr_temps.append(temps_dict)

    return jsonify(lastyr_temps)

@app.route("/api/v1.0/<start_date>")
def start(start_date):

    session = Session(engine)

    results = session.query(func.min(Measurement.tobs).label('TMIN'), func.avg(Measurement.tobs).label('TAVG'), func.max(Measurement.tobs).label('TMAX')).\
        filter(Measurement.date >= start_date).all()
   
    session.close()

    temp_summary = []
    for TMIN,TMAX,TAVG in results:
        temps_dict = {}
        temps_dict["TMIN"] = TMIN
        temps_dict["TMAX"] = TMAX
        temps_dict["TAVG"] = TAVG
        temp_summary.append(temps_dict)

    return jsonify(temp_summary)

@app.route("/api/v1.0/<start_date>/<end_date>")
def calc_temps(start_date, end_date):

    session = Session(engine)

    results = session.query(func.min(Measurement.tobs).label('TMIN'), func.avg(Measurement.tobs).label('TAVG'), func.max(Measurement.tobs).label('TMAX')).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
   
    session.close()

    temp_summary = []
    for TMIN,TMAX,TAVG in results:
        temps_dict = {}
        temps_dict["TMIN"] = TMIN
        temps_dict["TMAX"] = TMAX
        temps_dict["TAVG"] = TAVG
        temp_summary.append(temps_dict)

    return jsonify(temp_summary)


if __name__ == '__main__':
    app.run(debug=True)



