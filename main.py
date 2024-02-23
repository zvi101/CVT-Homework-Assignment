from flask import Flask, render_template, request
from flask_socketio import SocketIO



app = Flask(__name__)
app.config["SECRET_KEY"] = "secretKey"
socketio = SocketIO(app)



@app.route("/", methods=["POST", "GET"])
def home():
    session.clear()
    if request.method == "POST":
       name = request.form.get("name")
       code = request.form.get("code")
       join = request.form.get("join", False)
       create = request.form.get("create", False)

        # Error checking
       if not name:
          return render_template("home.html", error="Please enter a name.", code=code, name=name)
       if join != False and not code:
          return render_template("home.html", error="Please enter a room code.", code=code, name=name)
       

       room = code
        if create != False:
            room = generate_unique_code(4)
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
            return render_template("home.html", error="Room does not exist.", code=code, name=name)
       
        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))
       

    return render_template("home.html")


if __name__ == "__main__":
    socketio.run(app, debug=True)