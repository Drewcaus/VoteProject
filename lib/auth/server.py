from flask import Flask, request
import flask
import db
app = Flask(__name__)
@app.route("/")
def hello():
	return "Hello this is Flask Auth! CHANGES"

@app.route("/list/<inn>")
def ls(inn):
	lss = db.list()
	index = int(inn)
	
	if not index:
		return flask.jsonify(**lss[0])
	else:
		return flask.jsonify(**lss[index])

@app.route("/auth",methods=["GET"])
def auth():
	resp = request.json
	res = str(resp["hash"])
	if hash in resp:
		return res
	else:
	#return flask.jsonify(**resp)
		return "NA"
if __name__ == "__main__":
	app.run()
