# -*- coding: utf-8 -*-

import jieba
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/answer', methods=['POST'])
def answer():
    question = request.form['q'].encode('utf8')
    sep_list = jieba.cut(question)
    result = '/ '.join(sep_list).encode('utf8')
    return "<b>问句</b> " + question + " <b>分词结果:</b> " + result

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)
