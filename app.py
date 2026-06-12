from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"congratulations": "your flask app is running in a container! with blue/green deployment strategy  "}

@app.route("/health")
def health():
    return {"healthy": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)