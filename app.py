from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.highwayproject

@app.route('/')
def home():
   return render_template('indexnew.html')

@app.route('/boardnew.html')
def recommend():
   return render_template('boardnew.html')

@app.route('/indexnew.html')
def indexnew():
   return render_template('indexnew.html')

@app.route('/introduce_member.html')
def introduce():
   return render_template('introduce_member.html')

## API 역할을 하는 부분
@app.route('/boardnew', methods=['POST'])
def writerecommend():
    title_receive = request.form['title_give']
    writer_receive = request.form['writer_give']
    highway_receive = request.form['highway_give']
    comment_receive = request.form['comment_give']

    doc = {
        'title':title_receive,
        'writer':writer_receive,
        'highway':highway_receive,
        'comment':comment_receive
    }

    db.recommend.insert_one(doc)
    return jsonify({'msg': '제안해주셔서 감사합니다!'})


@app.route('/boardnew', methods=['GET'])
def showrecommend():
    recommendation = list(db.recommend.find({}, {'_id': False}))
    return jsonify({'all_recommendation': recommendation})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

