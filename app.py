from flask import Flask, render_template

app = Flask(__name__)




@app.route("/")
def index():

    BOARDS = dict(
        bw = dict (
            img = "black.png",
            url = "/bw",
            text = "Black & White",
        ),
        blue = dict (
            img = "blue.png",
            url = "blue",
            text = "Blue",
        ),
        red = dict (
            img = "red.png",
            url = "red",
            text = "Red",
        ),
        green = dict (
            img = "green.png",
            url = "green",
            text = "Green",
        ),
        yellow = dict (
            img = "yellow.png",
            url = "yellow",
            text = "Yellow",
        ),
        brown = dict (
            img = "brown.png",
            url = "brown",
            text = "Brown",
        )
    )

    return render_template("index.html", boards=BOARDS)