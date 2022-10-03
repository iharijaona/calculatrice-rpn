from .config import Config

def create_app():
    """Instantiation of the flask application"""

    from flask import Flask
    from flask_restx import Api

    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['ERROR_404_HELP'] = False

    from .api.operand import api as op_api
    from .api.stack import api as stack_api


    app_restx = Api(
        app,
        version='1.0',
        title=Config.APP_NAME,
        description=Config.APP_DESC,
        doc="/",
        prefix="/",
    )

    app_restx.add_namespace(op_api)
    app_restx.add_namespace(stack_api)

    return app
