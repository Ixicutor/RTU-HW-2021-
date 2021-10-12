import flask
from flask import request, jsonify,make_response
import requests,json
app = flask.Flask(__name__)
app.config["DEBUG"] = True

	
data={
"course": 411,
"courseName": "Software in Telecommunications",
"releaseYear": 2021,
"courseActive": True,
"droppedStudents": None,
"date": 20210218,
"data": [[11,2], [22, 4], [33, 1], [44,5]],
"scores": {"a":77, "b":46, "c":91}
}








@app.route('/', methods=['GET'])
def home():
    return "<h1>Telecommunication Sofware</h1><p>This site is a prototype API for data scores.</p>"



@app.route('/api/data', methods=['GET'])
def api_all():
    return jsonify(data)

@app.route('/api/data/scores', methods=['GET'])
def api_scores():
    return jsonify(data["scores"])

@app.route('/api/data/scores/<int:n>', methods=['GET'])
def getn_scores(n):
    l = list(data["scores"])[n]
    return jsonify({list(data["scores"])[n]: (data["scores"])[l]})

@app.route('/api/data/scores', methods=['POST'])
def post_scores():
    sc=request.json['sc']
    val=request.json['value']
    data['scores'][str(sc)]=val
    res = make_response(jsonify({"message": "data replaced"},{sc:val}), 200)
    return res


@app.route('/api/data/scores/<int:n>', methods=['PUT'])
def put_scores(n):
    sc=request.json['sc']
    val=request.json['value']
    l = list(data["scores"])[n]
    data['scores'][str(sc)]=(data["scores"]).pop(l)
    data['scores'][str(sc)]=val
    res = make_response(jsonify({"message": "data updated"},{sc,val}), 200)
    return res


@app.route('/api/data/scores/<int:n>', methods=['PATCH'])
def patch_scores(n):
    val=request.json['value']
    l = list(data["scores"])[n]
    data['scores'][l]=val
    res = make_response(jsonify({list(data["scores"])[n]: val}), 200)
    return res





@app.route('/api/data/scores/<int:n>', methods=['DELETE'])
def del_score(n):
    l = list(data["scores"])[n]
    (data["scores"]).pop(l)
    return make_response(jsonify({"message": "data deleted"}), 200)


app.run()



