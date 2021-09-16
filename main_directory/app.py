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

@app.route('/highwaylist.html')
def highwaylist():
   return render_template('highwaylist.html')

## API 역할을 하는 부분
@app.route('/boardnew', methods=['POST'])
def writerecommend():
    title_receive = request.form['title_give']
    writer_receive = request.form['writer_give']
    highway_receive = request.form['highway_give']
    comment_receive = request.form['comment_give']
    menu_receive = request.form['menu_give']

    doc = {
        'title':title_receive,
        'writer':writer_receive,
        'highway':highway_receive,
        'comment':comment_receive,
        'menu': menu_receive
    }

    db.recommend.insert_one(doc)
    return jsonify({'msg': '제안해주셔서 감사합니다!'})


@app.route('/boardnew', methods=['GET'])
def showrecommend():
    recommendation = list(db.recommend.find({}, {'_id': False}))
    return jsonify({'all_recommendation': recommendation})

@app.route('/api/list', methods=['GET'])
def show_stars():
    movie_star = list(db.lats1.find({}, {'_id': False}).sort("like", -1).limit(3))
    return jsonify({'movie_stars': movie_star})

@app.route('/api/lists', methods=['GET'])
def show_starss():
    movie_star = list(db.lats1.find({}, {'_id': False}).sort("like", -1))
    return jsonify({'movie_starss': movie_star})


@app.route('/api/like', methods=['POST'])
def like_highway():
    name_receive = request.form['name_give']

    target_highway = db.lats1.find_one({'name': name_receive})
    current_like = target_highway['like']

    new_like = current_like + 1

    db.lats1.update_one({'name': name_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': '좋아요 완료!'})

@app.route('/main', methods=['GET'])
def read_reviews():
    latlng = list(db.latlng.find({}, {'_id': False}))
    return jsonify({'latlng_all':latlng})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)

