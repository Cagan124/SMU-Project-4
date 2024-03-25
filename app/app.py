from flask import Flask, render_template, redirect
import pandas as pd
from flask import Flask, render_template, redirect, jsonify, request
from modelHelper import ModelHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
modelHelper = ModelHelper()

#################################################
# Flask Routes
#################################################

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/spotify_recommender")
def spotify_recommender():
    return render_template("spotify_recommender.html")


@app.route("/tableau01")
def tabeau01():
    # Return template and data
    return render_template("tableau01.html")

@app.route("/tableau02")
def tableau02():
    # Return template and data
    return render_template("tableau02.html")

@app.route("/about_us")
def about_us():
    # Return template and data
    return render_template("about_us.html")

@app.route("/works_cited")
def works_cited():
    # Return template and data
    return render_template("works_cited.html")

@app.route("/write_up")
def write_up():
    # Return template and data
    return render_template("write_up.html")

@app.route("/makePredictions", methods=["POST"])
def make_predictions():
    content = request.json["data"]
    print(content)
    # parse
    track_name = content["track_name"]
    track_artist = content["track_artist"]
    
    preds = modelHelper.makePredictions(track_name, track_artist)
    return(jsonify({"ok": True, "prediction":preds}))

#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
