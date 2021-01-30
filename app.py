import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session,
    url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["DB_NAME"] = os.environ.get("DB_NAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/", methods=["GET", "POST"])
def login():
    # If the post method is invoked by the submit button
    if request.method == "POST":
        # Check if the username is already taken
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username")})
        # If it exists confirms the pwd and creates session user
        if user_exists:
            if check_password_hash(
                    user_exists["password"], request.form.get("password")):
                session["wft_user"] = request.form.get("username"),
                flash("Logged in as {}".format(session["wft_user"][0]))
                # Takes the logged in user to the recipes page
                return redirect(url_for(
                                "recipes", username=session["wft_user"][0]))
            else:
                flash("Incorrect credentials. Try again or create new account")
                return redirect(url_for("login"))

        else:
            flash("Incorrect credentials. Try again or create new account")
            return redirect(url_for("login"))
    try:
        session["wft_user"]
        return redirect(url_for("recipes"))
    except Exception:
        return render_template("login.html")


@app.route("/logout")
def logout():
    # Removes the wft_user from session cookies
    session.pop("wft_user"),
    flash("You have logged out. Enter credentails to login again."),
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    # If the post method is invoked by the submit button
    if request.method == "POST":
        # Check if the username is already taken
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username")})
        # If it is taken create a flash message to inform the user
        if user_exists:
            flash("Username unavailable, enter another")
            # return to register page
            return redirect(url_for("register"))

        # Create an object from the create account form
        new_user = {
            "username": request.form.get("username"),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "password": generate_password_hash(request.form.get("password"))
        }
        # Insert the object as a doc in the database
        mongo.db.users.insert_one(new_user)

        # Place username into a session cookie for access to data
        session["wft_user"] = request.form.get("username")
        # Inform the user they successfully created an account
        flash("Account Created! You are now Logged in.")
        # Redirect user to recipes page
        return redirect(url_for("recipes", username=session["wft_user"]))
    return render_template("register.html")


@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/recipe_view/<recipe_id>")
def recipe_view(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe_view.html", recipe=recipe)


@app.route("/recipe_create", methods=["GET", "POST"])
def recipe_create():
    if request.method == "POST":
        # Script to create a list of shared with from multiple sources
        shared = []
        # Adds owner to shared_with list
        shared.append(session["wft_user"][0])
        # Gets the total length of the form
        form_length = len(request.form)
        # Sets i to 1
        i = 1
        # While i is less than form length
        while i <= form_length:
            # sets a unique key based on i
            shared_key = "shared_with" + str(i)
            # gets the value of the input for the unique key
            value = request.form.get(shared_key)
            # checks there is a value
            if value is not None:
                # appends the value to the shared_with list
                shared.append(request.form.get(shared_key))
            # increments the while loop
            i += 1

        # Script to create a list of objects containing ingredients
        ingredients = []
        # Gets the total length of the form
        form_length = len(request.form)
        # Sets i to 1
        i = 1
        # While i is less than form length
        while i <= form_length:
            # Creates an empty object
            ingredient = {}
            # Sets the unique key for ingredient_name in a variable
            ingredient_key = "ingredient_name" + str(i)
            # Sets the unique key for ingredient_quantity in a variable
            quantity_key = "ingredient_quantity" + str(i)
            # Sets the unique key for ingredient_unit in a variable
            unit_key = "ingredient_unit" + str(i)
            # Sets the value of the input for unique ingredient_name
            value = request.form.get(ingredient_key)
            # checks there is a value
            if value is not None:
                # Sets the value of ingredient_name in a variable
                ingredient_name = request.form.get(ingredient_key)
                # Sets the value of ingredient_quantity in a variable
                ingredient_quantity = request.form.get(quantity_key)
                # Sets the value of ingredient_unit in a variable
                ingredient_unit = request.form.get(unit_key)
                # Puts new Key/Value pairs in ingredient object
                ingredient["ingredient"] = ingredient_name
                ingredient["quantity"] = ingredient_quantity
                ingredient["unit"] = ingredient_unit
                # Appends object to list
                ingredients.append(ingredient)
            # increments the while loop
            i += 1

        # Creates the recipe object to send to MongoDB
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "region_of_origin": request.form.get("origin"),
            "classification": request.form.get("classify"),
            "image_url": request.form.get("image_url"),
            "image_description": request.form.get("image_description"),
            "description": request.form.get("description"),
            "ingredients": ingredients,
            "method": "",
            "owner": session["wft_user"][0],
            "shared_with": shared
        }
        # Sends the object ot MongoDB
        mongo.db.recipes.insert_one(recipe)
        # Lets the user know the object has been sent
        flash("Created New Recipe")
        # Takes the user back to the recipes page to see their recipes
        return redirect(url_for("recipes"))
    # Gets the list of classifications from MongoDB to send to the create page
    classification = mongo.db.classification.find().sort("class_name", 1)
    # Gets the list of origins from MongoDB to send to the create page
    origin = mongo.db.origin.find().sort("origin", 1)
    # Gets the list of units from MongoDB to send to the create page
    units = mongo.db.units.find().sort("unit", 1)
    return render_template(
        "recipe_create.html",
        classification=classification, origin=origin, units=units)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)
