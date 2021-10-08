from flask import Flask, render_template, redirect

app = Flask(__name__)

BOARDS = dict(
        bw = dict (
            img = "black.png",
            url = "bw",
            text = "Black & White",
            logo = "circle_dual_adjusted_edit.svg",
        ),
        blue = dict (
            img = "blue.png",
            url = "blue",
            text = "Blue",
            logo = "circle_edit.svg",
        ),
        red = dict (
            img = "red.png",
            url = "red",
            text = "Red",
            logo = "circle_edit.svg",
        ),
        green = dict (
            img = "green.png",
            url = "green",
            text = "Green",
            logo = "circle_edit.svg",
        ),
        yellow = dict (
            img = "yellow.png",
            url = "yellow",
            text = "Yellow",
            logo = "circle_edit.svg",
        ),
        brown = dict (
            img = "brown.png",
            url = "brown",
            text = "Brown",
            logo = "circle_edit.svg",
        )
    )


@app.context_processor
def create_menu():

    return dict(BOARDS=BOARDS)



@app.route("/", methods=["GET"])
def index():

    return render_template("index.html")


@app.route("/board/<board>", methods=["GET"])
def board(board):

    return render_template(f"{board}.html")

@app.route("/board", methods=["GET"])
def board_only():

    return redirect("/")