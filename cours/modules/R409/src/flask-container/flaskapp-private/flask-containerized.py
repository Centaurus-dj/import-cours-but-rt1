from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Le Python c'est bon, mangez en.\n"

@app.route("/whoami")
def get_task():
    ipv4 = os.popen("ip add show eth0").read().strip().split("inet")[1].split("/")[0].strip()
    return jsonify({"ip_hote": ipv4}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)