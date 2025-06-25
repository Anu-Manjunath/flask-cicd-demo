#Flask: The main web framework.
#jsonify: Converts Python dictionaries to JSON responses.
#socket: Used to get hostname and IP address.
#platform: Fetches system/OS info.
#psutil: A great library to get system performance info like memory and CPU usage.

from flask import Flask, jsonify
import socket
import platform
import psutil

#This initializes a Flask application called app.
app = Flask(__name__)

#This is a basic route. When someone visits http://localhost:5000/, it returns a plain greeting.
#You can replace this with an HTML dashboard later if you want.

@app.route('/')
def home():
    return "Welcome to the DevOps Monitoring App!"

@app.route('/info')
def system_info():
    info = {
        "hostname": socket.gethostname(), #Returns the machine's name (e.g., ip-172-31-xx-xx)
        "ip_address": socket.gethostbyname(socket.gethostname()), #Gets the IP address for that hostname
        "platform": platform.system(), #Returns OS name (e.g., Linux, Windows)
        "platform_release": platform.release(), #Returns OS version (e.g., 5.15.0-75-generic)
        "cpu_cores": psutil.cpu_count(), #Number of CPU cores
        "memory": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB" #Total RAM in bytes — we convert it to GB using 1024 ** 3
    }
    return jsonify(info) #Converts the dictionary to a JSON HTTP response

#This line runs the app.
#host='0.0.0.0': Makes the app available to external systems (like when deployed in Docker or EC2).
#port=5000: App will run on port 5000.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
