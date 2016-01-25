# -*- coding: utf-8 -*-

import jieba
import jieba.analyse
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/wordsplit', methods=['POST'])
def wordsplit():
    question = request.form['q'].encode('utf8')
    sep_list = jieba.cut(question)
    result = '/ '.join(sep_list).encode('utf8')
    return "<b>问句</b> " + question + " <br/><b>分词结果:</b> " + result


@app.route('/keyword', methods=['POST'])
def keyword():
    question = request.form['q'].encode('utf8')
    tags = jieba.analyse.extract_tags(question)
    result = ','.join(tags).encode('utf8')
    return "<b>问句</b> " + question + "<br/><b>关键字:</b> " + result

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
