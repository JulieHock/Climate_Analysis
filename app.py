from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

# import dependencies
import datetime as dt
import numpy as np
import pandas as pd

#import sqlalchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
