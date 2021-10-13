from datetime import datetime
from re import A
import sqlite3
from flask import Flask, render_template, redirect, g

app = Flask(__name__)

# Information about the different coloured boards  to be used on pages
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

# Constant with the columns in the database
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

# Add the BOARDS constant to all pages as it is used for the navbar
@app.context_processor
def add_info():
    year = datetime.now().strftime("%Y")

    return dict(BOARDS=BOARDS, year=year)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/board/<colour>", methods=["GET"])
def board(colour):
    """
    Retrieve the data for the selected colour from the DB and render the 
        template for the selected colour using the data
    """

    # Select relevant columns to put into the table
    TABLE_COLUMNS = COLUMNS[8:-1]

    # Get colour data from the database
    colours = select_colour_data(colour)

    return render_template("board.html", colours=colours, table_columns=TABLE_COLUMNS)


# If there is no color specified, redirect to index
@app.route("/board", methods=["GET"])
def board_only():
    return redirect("/")



# Helper functions

# Database management adapted from https://stackoverflow.com/a/16601526
def request_connection():
    """
    Request a connection to the database
    """

    # If there is no connection in the global ("g") variable, try to establish it
    if not hasattr(g, "conn"):
        g.conn = None
        try:
            g.conn = sqlite3.connect(DATABASE)
        except Exception as e:
            print(e)

    return g.conn

@app.teardown_request
def close_db_connection(ex):
    """
    Close the database connection
    """

    # Get the current connection
    conn = request_connection()
    conn.close()


def select_colour_data(colour):
    """
    Get the colour data from the database given the supplied colour name
    """

    # If the colour is "bw", get the black and white colours, otherwise get the 
    # supplied colour
    if colour == "bw":
        colours = ["black", "white"]
    else:
        colours = [colour]


    data = {}

    for col in colours:
        # Get all the information for the selected colour from the database
        conn = request_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Pigments WHERE colour=?", (col,))

        rows = cur.fetchall()

        colour_data = []
        for row in rows:
            # Pair the data with the column names in a dictionary
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
        
        # Add the colour data for the current colour
        data[col] = colour_data

    return data


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True, threaded=True)