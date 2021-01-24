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


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # If the post method is invoked by the submit button
    if request.method == "POST":
        # Check if the username is already taken
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
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
        session["wft_user"] = request.form.get("username").lower()
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


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)
