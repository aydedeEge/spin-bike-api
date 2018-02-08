#Imported libraries
from flask import Flask
from flask_restful import Resource, Api

#Imported local files
from hello_world import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)