from flask import Flask
from flask_cors import CORS


# initialize cors origin
cors = CORS()


def create_app():
    # Initialize Flask APP
    app = Flask(__name__)

    # Load cors into app
    cors.init_app(app)

    from .all_routes import bp  # Import the blueprint

    app.register_blueprint(bp)  # Register the blueprint

    return app
