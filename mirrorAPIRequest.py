from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        josn_request = request.get_json()
        return {'you get what you sent':josn_request}, 200

    def post(self):
        josn_request = request.get_json()
        return {'you sent':josn_request}, 200

class Multi(Resource):
    def get(self, num):
        return {'restful':num*10}

api.add_resource(HelloWorld,'/')
api.add_resource(Multi,'/multi/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)