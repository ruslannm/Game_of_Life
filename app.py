from flask import Flask, render_template, request
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():  # put application's code here
    width = 20
    height = 20
    if request.method == 'POST':
        width = int(request.form["width"])
        height = int(request.form["height"])
    GameOfLife(width=width, height=height)
    return render_template("index.html", width=width, height=height)


@app.route('/live')
def live():  # put application's code here
    width = request.args.get('width', default=20, type=int)
    height = request.args.get('height', default=20, type=int)
    if width != 20 or height != 20:
        life = GameOfLife(width=width, height=height)
    else:
        life = GameOfLife()
    if life.counter > 0:
        life.form_new_generation()
    life.counter += 1
    return render_template("live.html", life=life, width=width, height=height)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
