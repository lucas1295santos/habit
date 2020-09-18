from flask import Flask
from flask_restful import Api, Resource

# Declares the app
app = Flask(__name__)
api = Api(app)

# Resource is a baseclass where you can override the http methods
class Hello(Resource):
    def get(self):
        return {"data": "Saying hello!"}

api.add_resource(Hello, "/hello")

if __name__ == "__main__":
    app.run(debug=True)
