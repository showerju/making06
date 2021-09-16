from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
#client = MongoClient('localhost', 27017)
#db = client.test
client = MongoClient('localhost', 27017)
db = client.highwayproject


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('naver_map.html')
#고속도로 DB
@app.route('/main/01', methods=['GET'])
def fast01():
    latlng1 = list(db.latlng1.find({}, {'_id': False}))
    return jsonify({'latlng_all1':latlng1})

@app.route('/main/02', methods=['GET'])
def fast02():
    latlng2 = list(db.latlng2.find({}, {'_id': False}))
    return jsonify({'latlng_all2':latlng2})

@app.route('/main/03', methods=['GET'])
def fast03():
    latlng3 = list(db.latlng3.find({}, {'_id': False}))
    return jsonify({'latlng_all3':latlng3})

@app.route('/main/04', methods=['GET'])
def fast04():
    latlng4 = list(db.latlng4.find({}, {'_id': False}))
    return jsonify({'latlng_all4':latlng4})
#---------------------------------------------------------

@app.route('/main_info', methods=['GET'])
def parking_info():
    parking = list(db.lats1.find({}, {'_id': False}))
    return jsonify({'parking_all':parking})






if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
