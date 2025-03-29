from flask import Flask, render_template, jsonify, redirect, request, session
from dotenv import load_dotenv
import os

import utils

load_dotenv()
app = Flask(__name__, template_folder="templates")
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    location = session.get('location', None)
    mapbox_token = os.getenv('MAPBOX_ACCESS_TOKEN')
    return render_template('report.html', location=location, mapbox_token=mapbox_token)

@app.route('/submit', methods=['POST'])
def submit():
    reportdate = request.form.get('reportdate')
    location = list(map(float, request.form.get('location').strip().split(",")))
    details = request.form.get('details')
    status = "open"

    session['location'] = location

    utils.add_data(utils.report(reportdate, location, details, status))

    return redirect('/report')

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


if __name__ == "__main__":
    app.run()