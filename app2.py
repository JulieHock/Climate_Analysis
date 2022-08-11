#import Flask
from flask import Flask, jsonify
#define Flask App
app=Flask(__name__)

#define welcome route
@app.route("/")

#add routing information
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/temp/start/end
    ''')