from flask import Flask

def create_app():
    app = Flask(__name__)

    from test_blueprints.get.routes import get
    from test_blueprints.post.routes import post

    app.register_blueprint(get)
    app.register_blueprint(post)

    return app