from flask import Flask
import socket
import datetime

app = Flask(__name__)

with open("version.txt") as f:
    version = f.read()

@app.route("/")
def home():
    return f"""
    <h2>Blue-Green Deployment Demo</h2>
    <p>Version: {version}</p>
    <p>Server: {socket.gethostname()}</p>
    <p>Time: {datetime.datetime.now()}</p>
    """

app.run(host="0.0.0.0", port=5000)
