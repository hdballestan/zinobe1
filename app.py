from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3
import requests
import pandas as pd
import json
from prueba import *
app=Flask(__name__)

headings = ("T Total", "T medio", "T Min", "T Max")
data = ((str(tiempoTotal), str(media), str(minimo), str(maximo)))
@app.route('/', methods = ['POST', 'GET'])
def table():
    return render_template('table.html', tables = [df.to_html(classes='tablaC')], titles = [df.columns.values], headings=headings, data=data)


if __name__ == '__main__':
    app.run(debug=True)