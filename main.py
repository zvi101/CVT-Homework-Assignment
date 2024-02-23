from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config["SECRET"] = "secretKey"
socketio = SocketIO(app)


@socketio.on('message')
def printMessage(message):
    print('Enter message: ' + message)
    if message != 'user connected':
        send(message, broadcast=True)


@app.route('/')
def index():
    return render_template('index.html')

 
if __name__ == "__main__":
    socketio.run(app, host="localhost")