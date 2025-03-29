from flask import Flask, render_template, jsonify, redirect, request, session
import os
from dotenv import load_dotenv

import utils

load_dotenv()
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = os.urandom(24)

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/map/download', endpoint='office_map_download')
def office_map_download():
    return render_template('office_map_download.html')

@app.route('/icefreezone')
def icefreezone():
    return render_template('icefreezone.html')

@app.route('/map')
def map_view():
    mapbox_secret = os.getenv('MAPBOX_SECRET')
    location = session.get('location', None)
    return render_template('map.html', location=location, mapbox_secret=mapbox_secret)

@app.route('/report')
def report():
    location = session.get('location', None)
    mapbox_secret = os.getenv('MAPBOX_SECRET')
    return render_template('report.html', location=location, mapbox_secret=mapbox_secret)

@app.route('/reportsuccess')
def report_success():
    location = session.get('location', None)
    if location:
        session.pop('location', None)
    return render_template('reportsuccess.html', location=location)

@app.route('/submit', methods=['POST'])
def submit():
    reportdate = request.form.get('reportdate')
    location = list(map(float, request.form.get('location').strip().split(",")))
    details = request.form.get('details')
    status = "open"

    session['location'] = location

    utils.add_data(utils.report(reportdate, location, details, status))

    return redirect('/reportsuccess')

@app.route('/api', methods=['GET'])
def api():
    return jsonify({
        "name": "beacon",
        "status": "success",
        "endpoints": ["data"],
        "src": 'https://github.com/calebyhan/solhacks25'
    })

@app.route('/api/data', methods=['GET'])
def data():
    i = request.args.get('i', default=100)
    startDate = request.args.get('startDate', default=None)
    endDate = request.args.get('endDate', default=None)
    
    result = utils.get_data(i, startDate, endDate)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run()