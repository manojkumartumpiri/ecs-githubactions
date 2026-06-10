from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "ok", "service": "ecr", "version-automated-image tag": "4.0.0"}

@app.route("/health")
def health():
    return {"healthy": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)