# 1. imports
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

#################################################
# Flask Setup
#################################################
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to my 'Home' page!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/[start_date:ddmmyyyy]<br/>"
        f"/api/v1.0/[start_date:ddmmyyyy]/[end_date:ddmmyyyy]<br/>"
    )


# 4. Define what to do when a user his the various routes
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Convert query results from Jupyter precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>='2016-08-23').filter(Measurement.date<='2017-08-23').all()
    
    session.close()
    
    year_prcp = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict['date'] = date
        prcp_dict['prcp'] = prcp
        year_prcp.append(prcp_dict)

    # Return the JSON representation of the dictionary.
    return jsonify(prcp_dict)


@app.route("/api/v1.0/stations")
def stations():
    
    """Return a list of stations"""
    #Query all stations
    results = session.query(Station.station).all()

    session.close()
    
    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))
        
    # Return a JSON list of stations from the dataset.
    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():

    # Query the dates and temperature observations of the most-active station for the previous year of data.
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date>='2016-08-23').filter(Measurement.date<='2017-08-23').filter(Measurement.station == "USC00519281").all()
    
    session.close()
    
    year_temp = []
    for date, tobs in results:
        temp_dict = {}
        temp_dict['date'] = date
        temp_dict['tobs'] = tobs
        year_temp.append(temp_dict)
    
    # Return a JSON list of temperature observations for the previous year.
    return jsonify(temp_dict)


@app.route("/api/v1.0/<start_date>")
@app.route("/api/v1.0/<start_date>/<end_date>")
def start(start_date=None, end_date=None):
    
    #return f"start_date: " + start_date
    if not end_date:
        
        start_date_format = dt.datetime.strptime(start_date, "%m%d%Y")

        # For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date_format).all()
        print(results)
        session.close()
        
        start_calc = []
        for smin, savg, smax in results:
            start_dict = {}
            start_dict['Min'] = smin
            start_dict['Avg'] = savg
            start_dict['Max'] = smax
            start_calc.append(start_dict)

        # Return the JSON representation of the dictionary.
        return jsonify(start_dict)

    start_date = dt.datetime.strptime(start_date, "%m%d%Y")
    end_date = dt.datetime.strptime(end_date, "%m%d%Y")

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date>=start_date).filter(Measurement.date<=end_date).all()
    
    session.close()

    end_dict = list(np.ravel(results))

    return jsonify(end_dict)


if __name__ == "__main__":
    app.run(debug = True)