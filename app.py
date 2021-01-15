from flask import Flask, render_template, request
import sqlite3
import requests
import pandas as pd
import json
from prueba import *
app=Flask(__name__)

headings = ("Region", "City Name", "Languaje", "Time")



@app.route('/')
def table():
    return render_template('table.html', headings=headings)


if __name__ == '__main__':
    app.run(debug=True)