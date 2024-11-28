from flask import Flask, jsonify


def create_flask_app():
    server = Flask(__name__)
    register_flask_routes(server)
    return server


def register_flask_routes(app: Flask):
    @app.route("/")
    def main():
        return jsonify({"status": "OK"}, 200)
