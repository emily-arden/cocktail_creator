# import the request library
import requests
import json
import webbrowser

from flask import Blueprint, request, render_template

cocktail_routes = Blueprint("cocktail_routes", __name__)

# cocktail database api details by id
URL = "https://www.thecocktaildb.com/api/json/v1/1/lookup.php"
#
# GET /
#
@cocktail_routes.route("/")
def index():
    print("VISITING THE START PAGE")
    return render_template("start.html")

#
# GET /search/cocktail
# GET /search/cocktail?name=margarita
# POST /search/cocktail
#
@cocktail_routes.route("/search/cocktail", methods=["GET", "POST"])
def cocktail():
    print("VISITING THE SEARCH PAGE")
    print("REQUEST PARAMS:", dict(request.args))
    print("REQUEST VALUES:", dict(request.values))
    
    # defining a params dict for the parameters to be sent to the API

    if "id" in request.args:
        params = {"i":request.args["id"]}
    elif "id" in request.values:
        # HANDLE POST REQUEST WITH CHOICE IN THE REQUEST BODY:
        params = {"i":request.values["id"]}
        # sending get request and saving the response as response object
    else:
       return render_template("error.html")

    response = request.get(url = URL, params = params)
    data = response.json()
    print(data)

    return render_template("cocktail.html",
        data=data,
    )
