from flask import Flask, jsonify
import time
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(
        {"Time of Call": time.strftime("%H:%M:%S", time.localtime()),
        "Name" : "Sagnik",
        "Comment" : "I am learning Docker and Kubernetes",
        "Team" : "DockKube"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)