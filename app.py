from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    GameOfLife()
    return render_template("index.html")


@app.route('/live')
def live():  # put application's code here
    life = GameOfLife()
    if life.counter > 0:
        life.form_new_generation()
    life.counter += 1
    return render_template("live.html", life=life)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
