from flask import Flask, request, jsonify
import socket
import subprocess

app = Flask(__name__)

# Define a global variable to store the value of "num"
num_value = None

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    global num_value

    if request.method == 'GET':
        return f'{socket.gethostname()}'

    if request.method == 'POST':
        script_path = 'submit.py'
        process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return ""

if __name__ == '__main__':
    app.run(debug=True)

