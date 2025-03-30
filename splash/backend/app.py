from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder='frontend')

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')  # Serve the main entry point of your frontend

@app.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Splash Page API!"})

@app.route('/<path:path>', methods=['GET'])
def serve_static(path):
    # For serving static files like JS, CSS
    return send_from_directory('frontend', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)