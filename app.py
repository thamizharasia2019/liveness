from flask import Flask
from flask_restplus import Api, Resource
from flask import Flask,render_template,url_for,request

flask_app = Flask(__name__)
app = Api(app = flask_app)

name_space = app.namespace('main', description='Main APIs')

@name_space.route("/")
class MainClass(Resource):
	def get(self):

		return {
			"status": "Got new data"
		}
	def post(self):
		choice = request.form['taskoption']
		rawtext = request.form['rawtext']
		
if __name__ == '__main__':
	app.run(debug=True)		
