from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app)
    
    # Register blueprints
    # from app.routes.auth import auth_bp
    # from app.routes.investments import investments_bp
    # from app.routes.recommendations import recommendations_bp
    
    # app.register_blueprint(auth_bp, url_prefix='/api/auth')
    # app.register_blueprint(investments_bp, url_prefix='/api/investments')
    # app.register_blueprint(recommendations_bp, url_prefix='/api/recommendations')
    
    return app