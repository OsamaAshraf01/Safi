from flask import Flask
from config import DevelopmentConfig
from app.logging_config import configure_logging

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 1. Setup Logging BEFORE extensions
    configure_logging(app)
    app.logger.info("Starting up the application...")

    # ... rest of your code ...
    
    return app