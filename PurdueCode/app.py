from pymongo import MongoClient
import requests
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# mongoDB는 27017 포트로 돌아갑니다.
client = MongoClient('mongodb://test:test@18.116.64.150', 27017)
db = client.dbjungle  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    result = list(db.memos.find({}, {'_id': 0}))
    # 2. memos 키 값으로 memos 정보 보내주기
    return jsonify({'result': 'success', 'memos': result})


@app.route('/memo', methods=['POST'])
def saving():
    title_receive = request.form['title_give']  # 클라이언트로부터 url을 받는 부분
    content_receive = request.form['content_give']  # 클라이언트로부터 comment를 받는 부분
    memo = {'title': title_receive, 'content': content_receive}
    db.memos.insert_one(memo)
    return jsonify({'result': 'success'})


@app.route('/edit', methods=['POST'])
def edit_memo():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    title = request.form['title']
    content = request.form['content']
    n_title = request.form['n_title']
    n_content = request.form['n_content']

    db.memos.update_one({'title': title, 'content': content}, {
        '$set': {'title': n_title, 'content': n_content}})

    # 3. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})


@app.route('/delete', methods=['POST'])
def delete_memo():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    title = request.form['title']
    content = request.form['content']
    db.memos.delete_one({'title': title, 'content': content})
    # 3. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
