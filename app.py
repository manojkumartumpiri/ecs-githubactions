from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "ok", "service": "ecr-demo-v4-this is manoj", "version": "4.0.0"}

@app.route("/health")
def health():
    return {"healthy": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)