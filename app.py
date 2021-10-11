from re import A
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, g

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pigments.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

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

COLUMNS = [
        "id",
        "PCID",
        "Name",
        "Colour",
        "Alias",
        "Manufacturer",
        "URL",
        "Description",
        "Initial observations",
        "Colour & Translucency",
        "Opacity",
        "Resistance",
        "Stringiness",
        "Observations during grinding",
        "Details",
        "Shape",
        "Scratching",
        "Smoothness",
        "Impasto",
        "Grittiness",
        "Observations during application",
        "Colour intensity",
        "Glossiness",
        "Hiding power",
        "Tinting strength",
        "Observations during mixing with lead white",
        "Observations during application with lead white",
        "img_name",
    ]

DATABASE = "pigments.db"

# db = SQLAlchemy(app)
# db.create_all()

@app.context_processor
def create_menu():

    return dict(BOARDS=BOARDS)



@app.route("/", methods=["GET"])
def index():

    return render_template("index.html")


@app.route("/board/<colour>", methods=["GET"])
def board(colour):
    """
    Retreive the data for the selected colour from the DB
    """

    TABLE_COLUMNS = COLUMNS[8:-1]

    colours = select_colour_data(colour)

    return render_template("board.html", colours=colours, table_columns=TABLE_COLUMNS)


# If there is no color specified, redirect to index
@app.route("/board", methods=["GET"])
def board_only():

    return redirect("/")



# Helper functions

# Database management adapted from https://stackoverflow.com/a/16601526
def get_request_connection():
    if not hasattr(g, "conn"):
        g.conn = None
        try:
            g.conn = sqlite3.connect(DATABASE)
        except Exception as e:
            print(e)

    return g.conn

@app.teardown_request
def close_db_connection(ex):
    conn = get_request_connection()
    conn.close()


def select_colour_data(colour):
    

    if colour == "bw":
        colours = ["black", "white"]
    else:
        colours = [colour]


    data = {}

    for col in colours:
        conn = get_request_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Pigments WHERE colour=?", (col,))

        colour_data = []

        rows = cur.fetchall()
        for row in rows:
            colour_data.append(dict(zip(COLUMNS, row)))
            
            # Reformat the alias field
            aliasses = colour_data[-1]["Alias"]
            if aliasses is not None:
                aliasses = aliasses.split(",")
                alias = ""
                for a in aliasses:
                    alias.append(a)
                    alias.append("  ·  ")
                alias = alias["-5"]
                colour_data[-1]["Alias"] = alias
        
        data[col] = colour_data

    return data


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True, threaded=True)