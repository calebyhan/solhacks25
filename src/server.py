from flask import Flask, render_template, jsonify, redirect, request
import utils

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/submit', methods=['POST'])
def submit():
    reportdate = request.form.get('reportdate')
    location = list(map(float, request.form.get('location').strip().split(",")))
    details = request.form.get('details')
    status = "open"

    print(reportdate, location, details, status)

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
