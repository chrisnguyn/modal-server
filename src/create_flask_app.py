from flask import Flask, jsonify


def create_flask_app():
    server = Flask(__name__)

    @server.route("/")
    def main():
        return jsonify({"status": "OK"}, 200)
