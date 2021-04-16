import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
api = Api(app)
cors = CORS(app, support_credentials=True)

jwt = JWTManager(app)

if __name__ == '__main__':
    if os.environ['ENV'] == 'dev':
        app.run(debug=True)
    else:
        app.run()
