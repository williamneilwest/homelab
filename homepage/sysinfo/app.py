from flask import Flask, jsonify
import psutil
import socket

app = Flask(__name__)

def get_system_info():
    return {
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage("/").percent,
        "hostname": socket.gethostname(),
        "local_ip": socket.gethostbyname(socket.gethostname())
    }

@app.route("/sysinfo", methods=["GET"])
def system_info():
    return jsonify(get_system_info())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)