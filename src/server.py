from flask import Flask, render_template, jsonify, request
import utils

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def api():
    return jsonify({
        "name": "beacon",
        "status": "success",
        "endpoints": ["data"],
        "src": '<a href="https://github.com/calebyhan/solhacks25">https://github.com/calebyhan/solhacks25</a>'
    })

@app.route('/api/data', methods=['GET'])
def data():
    i = request.args.get('i', default=100)
    startDate = request.args.get('startDate', default=None)
    endDate = request.args.get('endDate', default=None)
    
    result = utils.get_data(i, startDate, endDate)
    
    return jsonify(result)
