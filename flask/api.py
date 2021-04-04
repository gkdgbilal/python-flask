from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Flask(Resource):
    def get(self):
        return 'Hello World from Flask!'

api.add_resource(Flask, '/staj')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)