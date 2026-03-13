from flask import Flask
import socket
import datetime

app = Flask(__name__)

# Read version from file
try:
    with open("version.txt", "r") as f:
        version = f.read().strip()
except:
    version = "Unknown"

@app.route("/")
def home():
    hostname = socket.gethostname()
    current_time = datetime.datetime.now()

    return f"""
    <html>
        <head>
            <title>Blue-Green Deployment Demo</title>
            <style>
                body {{
                    font-family: Arial;
                    text-align: center;
                    margin-top: 100px;
                    background-color: #f4f6f8;
                }}
                .card {{
                    background: white;
                    padding: 40px;
                    border-radius: 10px;
                    width: 400px;
                    margin: auto;
                    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
                }}
            </style>
        </head>

        <body>
            <div class="card">
                <h2>Blue-Green Deployment Demo</h2>
                <p><b>Version:</b> {version}</p>
                <p><b>Server:</b> {hostname}</p>
                <p><b>Time:</b> {current_time}</p>
            </div>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
