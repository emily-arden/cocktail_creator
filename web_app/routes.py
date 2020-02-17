# import the request library
import requests
import json
import webbrowser
import pprint

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
# GET /search/cocktail?id=1111
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

    response = requests.get(url = URL, params = params)
    data = response.json()
    pprint.pprint(data)
    cocktail = data.get('drinks')[0]
    ingredients = []
    for i in range(1,16):
        if cocktail.get(f'strIngredient{i}') is None:
            break
        print(cocktail.get(f'strIngredient{i}') )
        ingredients.append(cocktail.get(f'strIngredient{i}') + ": " + (cocktail.get(f'strMeasure{i}') if cocktail.get(f'strMeasure{i}') is not None else 'personal preference'))
        print(ingredients)
    data['ingredients'] = ingredients
    return render_template("cocktail.html",
        data=data,
    )
