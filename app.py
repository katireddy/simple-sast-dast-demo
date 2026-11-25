from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(
        message="Simple SAST and DAST demo",
        endpoints=["/health", "/hello?name=Developer"],
    )

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

@app.get("/hello")
def hello():
    name = request.args.get("name", "Developer")
    return jsonify(message=f"Hello, {name}!"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
