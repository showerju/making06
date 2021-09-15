from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('naver_map.html')

@app.route('/main', methods=['GET'])
def read_reviews():
    parking = list(db.parking.find({}, {'_id': False}))
    latlng = list(db.latlng.find({}, {'_id': False}))
    return jsonify({'latlng_all':latlng,'parking_all':parking})




if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
