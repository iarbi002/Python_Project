from flask import Flask, session, redirect, url_for, escape, request
from flask import render_template
import planisphere

app = Flask(__name__)

@app.route("/")
def index():
    #this is used to setup the session with starting values
    session['room_name'] = planisphere.START
    print(session['room_name'])
    return redirect(url_for("game"))

@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')
    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
        else:
            #why is there here? do you need it?
            return render_template("you_died.html")
    else:
        action = request.form.get('action')
        print(f"action={action}")
        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)
            print(f"next_room={next_room}")
            if not next_room:
                try:
                    print(f"room.retryAttemptsLimit={room.retryAttemptsLimit}")
                    print(f"room.retryAttempts={room.retryAttempts}")
                    if int(room.retryAttemptsLimit) < room.retryAttempts:
                        if room.deathOnFailure:
                            return render_template("you_died.html")
                    else:
                        room.retryAttempts = int(room.retryAttempts) + 1
                except:
                    pass
                session['room_name'] = planisphere.name_room(room)
            else:
                session['room_name'] = planisphere.name_room(next_room)
        return redirect(url_for("game"))

#change if going live
app.secret_key='abc123'

if __name__ == "__main__":
    app.run()