from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@13.125.45.230', 27017)
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
    movie_star = list(db.lats1.find({}, {'_id': False}).sort("like", -1).limit(4))
    return jsonify({'movie_stars': movie_star})

@app.route('/api/lists', methods=['GET'])
def show_starss():
    movie_star = list(db.lats1.find({}, {'_id': False}).sort("like", -1))
    return jsonify({'movie_starss': movie_star})

@app.route('/main_info', methods=['GET'])
def parking_info():
    parking = list(db.lats1.find({}, {'_id': False}))
    return jsonify({'parking_all':parking})

@app.route('/api/like', methods=['POST'])
def like_highway():
    name_receive = request.form['name_give']

    target_highway = db.lats1.find_one({'name': name_receive})
    current_like = target_highway['like']

    new_like = current_like + 1

    db.lats1.update_one({'name': name_receive}, {'$set': {'like': new_like}})

    return jsonify({'msg': '좋아요 완료!'})
#
# @app.route('/')
# def home():
#     return render_template('naver_map.html')


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

@app.route('/main/05', methods=['GET'])
def fast05():
    latlng5 = list(db.latlng5.find({}, {'_id': False}))
    return jsonify({'latlng_all5':latlng5})

@app.route('/main/06', methods=['GET'])
def fast06():
    latlng6 = list(db.latlng6.find({}, {'_id': False}))
    return jsonify({'latlng_all6':latlng6})

@app.route('/main/07', methods=['GET'])
def fast07():
    latlng7 = list(db.latlng7.find({}, {'_id': False}))
    return jsonify({'latlng_all7':latlng7})

@app.route('/main/08', methods=['GET'])
def fast08():
    latlng8 = list(db.latlng8.find({}, {'_id': False}))
    return jsonify({'latlng_all8':latlng8})

@app.route('/main/09', methods=['GET'])
def fast09():
    latlng9 = list(db.latlng9.find({}, {'_id': False}))
    return jsonify({'latlng_all9':latlng9})

@app.route('/main/10', methods=['GET'])
def fast10():
    latlng10 = list(db.latlng10.find({}, {'_id': False}))
    return jsonify({'latlng_all10':latlng10})

@app.route('/main/11', methods=['GET'])
def fast11():
    latlng11 = list(db.latlng11.find({}, {'_id': False}))
    return jsonify({'latlng_all11':latlng11})

@app.route('/main/12', methods=['GET'])
def fast12():
    latlng12 = list(db.latlng12.find({}, {'_id': False}))
    return jsonify({'latlng_all12':latlng12})





if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
