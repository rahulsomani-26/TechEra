from flask import Flask,jsonify,request
import json

app = Flask(__name__)
with open('dummdata.json') as f:
    data = json.load(f)

@app.route('/get')
def send_details():
    return data


if __name__ == '__main__':
    app.run(debug=True)



