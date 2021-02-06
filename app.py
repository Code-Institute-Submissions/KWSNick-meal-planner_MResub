import os
import datetime
import calendar
from random import choice
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
    flash("You have logged out. Enter credentials to login again."),
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


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(
                mongo.db.recipes.find({"$text": {"$search": query}}))
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
                # checks the input field is not blank
                user_entry = request.form.get(shared_key)
                if user_entry != "":
                    # appends the value to the shared_with list
                    shared.append(user_entry)
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
                # checks the ingredient_name is not blank
                if ingredient_name != "":
                    # Puts name Key/Value pair in ingredient object
                    ingredient["ingredient"] = ingredient_name
                    # checks the ingredient_quantity is not blank
                    if ingredient_quantity != "":
                        # Puts quantity Key/Value pair in ingredient object
                        ingredient["quantity"] = ingredient_quantity
                    # checks the ingredient_unit is not blank
                    if ingredient_unit != "":
                        # Puts unit Key/Value pair in ingredient object
                        ingredient["unit"] = ingredient_unit
                    # Appends object to list
                    ingredients.append(ingredient)
            # increments the while loop
            i += 1

        # Script to create a list of method steps from multiple sources
        steps = []
        # Gets the total length of the form
        form_length = len(request.form)
        # Sets i to 1
        i = 1
        # While i is less than form length
        while i <= form_length:
            # sets a unique key based on i
            step_key = "step" + str(i)
            # gets the value of the input for the unique key
            value = request.form.get(step_key)
            # checks there is a value
            if value is not None:
                # checks the input field is not blank
                user_entry = request.form.get(step_key)
                if user_entry != "":
                    # appends the value to the steps list
                    steps.append(request.form.get(step_key))
            # increments the while loop
            i += 1

        # If no image url, use placeholder
        form_image_url = request.form.get("image_url")
        if form_image_url != "":
            image_url = request.form.get("image_url")
        else:
            image_url = "../static/images/recipe_img_pholder.png"

        # If no image alt text, use placeholder
        form_image_desc = request.form.get("image_description")
        if form_image_desc != "":
            image_desc = request.form.get("image_description")
        else:
            image_desc = "What's for tea placeholder image"

        # Creates the recipe object to send to MongoDB
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "region_of_origin": request.form.get("origin"),
            "classification": request.form.get("classify"),
            "image_url": image_url,
            "image_description": image_desc,
            "description": request.form.get("description"),
            "ingredients": ingredients,
            "method": steps,
            "owner": session["wft_user"][0],
            "shared_with": shared
        }
        # Sends the object to MongoDB
        mongo.db.recipes.insert_one(recipe)
        # Lets the user know the object has been sent
        flash("Created New Recipe")
        # Takes the user back to the recipes page to see their recipes
        return redirect(url_for("recipes"))
    # Gets the list of classifications from MongoDB to send to the create page
    classification = mongo.db.classification.find().sort("class_name", 1)
    # Gets the list of origins from MongoDB to send to the create page
    origin = mongo.db.origin.find().sort("origin", 1)
    return render_template(
        "recipe_create.html",
        classification=classification, origin=origin)


@app.route("/delete_recipe/<recipe_id>", methods=["GET", "POST"])
def delete_recipe(recipe_id):
    user = session["wft_user"][0]
    print(user)
    mongo.db.recipes.update(
        {"_id": ObjectId(recipe_id)},
        {"$pull": {"shared_with": user}})
    # Lets the user know the recipe has been removed
    flash("Recipe Successfully Deleted")
    return redirect(url_for("recipes"))


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        # Script to create a list of shared with from multiple sources
        shared = []
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
                # checks the input field is not blank
                user_entry = request.form.get(shared_key)
                if user_entry != "":
                    # appends the value to the shared_with list
                    shared.append(user_entry)
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
                # checks the ingredient_name is not blank
                if ingredient_name != "":
                    # Puts name Key/Value pair in ingredient object
                    ingredient["ingredient"] = ingredient_name
                    # checks the ingredient_quantity is not blank
                    if ingredient_quantity != "":
                        # Puts quantity Key/Value pair in ingredient object
                        ingredient["quantity"] = ingredient_quantity
                    # checks the ingredient_unit is not blank
                    if ingredient_unit != "":
                        # Puts unit Key/Value pair in ingredient object
                        ingredient["unit"] = ingredient_unit
                    # Appends object to list
                    ingredients.append(ingredient)
            # increments the while loop
            i += 1

        # Script to create a list of method steps from multiple sources
        steps = []
        # Gets the total length of the form
        form_length = len(request.form)
        # Sets i to 1
        i = 1
        # While i is less than form length
        while i <= form_length:
            # sets a unique key based on i
            step_key = "step" + str(i)
            # gets the value of the input for the unique key
            value = request.form.get(step_key)
            # checks there is a value
            if value is not None:
                # checks the input field is not blank
                user_entry = request.form.get(step_key)
                if user_entry != "":
                    # appends the value to the steps list
                    steps.append(request.form.get(step_key))
            # increments the while loop
            i += 1

        # If no image url, use placeholder
        form_image_url = request.form.get("image_url")
        if form_image_url != "":
            image_url = request.form.get("image_url")
        else:
            image_url = "../static/images/recipe_img_pholder.png"

        # If no image alt text, use placeholder
        form_image_desc = request.form.get("image_description")
        if form_image_desc != "":
            image_desc = request.form.get("image_description")
        else:
            image_desc = "What's for tea placeholder image"

        # Creates the recipe object to send to MongoDB
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "region_of_origin": request.form.get("origin"),
            "classification": request.form.get("classify"),
            "image_url": image_url,
            "image_description": image_desc,
            "description": request.form.get("description"),
            "ingredients": ingredients,
            "method": steps,
            "owner": session["wft_user"][0],
            "shared_with": shared
        }
        # Sends the object to MongoDB
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, recipe)
        # Lets the user know the object has been sent
        flash("Successfully Amended Recipe")
        # Takes the user back to the recipes page to see their recipes
        return redirect(url_for("recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # Gets the list of classifications from MongoDB to send to the edit page
    classification = mongo.db.classification.find().sort("class_name", 1)
    # Gets the list of origins from MongoDB to send to the edit page
    origin = mongo.db.origin.find().sort("origin", 1)
    return render_template(
        "recipe_edit.html",
        recipe=recipe, classification=classification, origin=origin)


@app.route("/weekly_menus", methods=["GET", "POST"])
def weekly_menus():
    c = calendar.Calendar()
    cal = ""
    months = calendar.month_name
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    month_name = months[month]
    if request.method == "POST":
        selected_year = int(request.form.get("year_select"))
        selected_month = int(request.form.get("month_select"))
        has_week = request.form.get("week_select")
        if has_week == "no weeks":
            cal = c.monthdayscalendar(selected_year, selected_month)
            month_name = months[selected_month]
            plans = list(
                    mongo.db.weekly_plans.find().sort("week_commencing", -1))
            recipes = list(mongo.db.recipes.find())
            return render_template(
                            "weekly_menus.html",
                            cal=cal, year=selected_year,
                            month=selected_month,
                            month_name=month_name,
                            plans=plans,
                            recipes=recipes)
        else:
            cal = c.monthdayscalendar(selected_year, selected_month)
            week = int(request.form.get("week_select"))
            days = cal[week]
            meals = []
            year = str(request.form.get("year_select"))
            month = str(request.form.get("month_select"))
            if len(month) == 1:
                month = "0" + month
            day = str(days[0])
            if len(day) == 1:
                day = "0" + day
            date = year + month + day
            recipes = list(
                        mongo.db.recipes.find(
                                    {"shared_with": session["wft_user"][0]},
                                    "_id"))
            for day in days:
                # thanks to machine learning mastery
                # for tips and advice
                # https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
                meal = choice(recipes)
                meals.append(meal)
            weekly_plan = {
                "owner": session["wft_user"][0],
                "week_commencing": date,
                "year": year,
                "month": month,
                "days": days,
                "meals": meals
            }
            # Sends the object to MongoDB
            mongo.db.weekly_plans.insert_one(weekly_plan)
            # Lets the user know the object has been sent
            flash("Created New Menu")
            # Takes the user back to the recipes page to see their recipes
            return redirect(url_for("weekly_menus"))
    plans = list(mongo.db.weekly_plans.find().sort("week_commencing", -1))
    recipes = list(mongo.db.recipes.find())
    return render_template(
                        "weekly_menus.html",
                        year=year,
                        month=month,
                        month_name=month_name,
                        plans=plans,
                        recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)
