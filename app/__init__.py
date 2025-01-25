from flask import Flask
from flask_restx import Api

def create_app():
    app = Flask(__name__)
    api = Api(app, title='PDF QA API', version='1.0', description='API for PDF Question Answering')
    
    from app.routes.api import api as pdf_api
    api.add_namespace(pdf_api, path='/api/v1')
    
    return app