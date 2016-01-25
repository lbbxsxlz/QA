# -*- coding: utf-8 -*-

import jieba
import jieba.analyse
import jieba.posseg as pseg

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
    tags = jieba.analyse.extract_tags(question, withWeight=True)
    result = "<b>问句</b> " + question + "<br/><b>关键字:</b>"
    for tag in tags:
        result += "{}({}), ".format(tag[0].encode('utf8'),
                                    tag[1])
    return result


@app.route('/pos', methods=['POST'])
def pos():
    question = request.form['q'].encode('utf8')
    words = pseg.cut(question)
    result = "<b>问句</b> " + question + "<br/><b>词性标注:</b>"
    for word, flag in words:
        word = word.encode('utf8')
        result += "{} {}, ".format(word, flag)
    return result

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
