from flask import Flask, render_template, jsonify, redirect, request, session
import os

import utils

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = os.urandom(24)  # Secret key to sign the session cookie



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map')
def map_view():
    return render_template('map.html')

@app.route('/report')
def report():
    location = session.get('location', None)  # Retrieve location from session
    return render_template('report.html', location=location)

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/icefreezone')
def icefreezone():
    return render_template('icefreezone.html')

@app.route('/submit', methods=['POST'])
def submit():
    reportdate = request.form.get('reportdate')
    location = list(map(float, request.form.get('location').strip().split(",")))
    details = request.form.get('details')
    status = "open"

    # Store location in session
    session['location'] = location

    # You can add the data to the utils here
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

if __name__ == '__main__':
    app.run()
