import flask
from flask import request, jsonify,make_response

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
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
@app.route('/api/resources/data/all', methods=['GET'])
def api_all():
    return jsonify(data)
@app.route('/api/resources/data/scores/', methods=['GET'])
def get_scores():
    sc=request.args.get('sc')
    print(sc)
    return jsonify(data['scores'][str(sc)])

@app.route('/api/resources/data/scores', methods=['POST'])
def post_scores():
    sc=request.json['sc']
    val=request.json['value']
    data['scores'][str(sc)]=val
    res = make_response(jsonify({"message": "data replaced"}), 200)
    return res


@app.route('/api/resources/data/scores/<int>', methods=['PUT'])
def put_scores():
    sc=request.json['sc']
    val=request.json['value']
    data['scores'][str(sc)]=val
    res = make_response(jsonify({"message": "data updated"}), 200)
    return res




app.run()



