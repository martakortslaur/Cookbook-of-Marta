import os
from flask import Flask, request, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'cookbook_database'    # name of your database
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb+srv://marta_korts_laur:AstelV88l@cluster0-utrzr.mongodb.net/test?retryWrites=true&w=majority')   # URI (see above)
mongo = PyMongo(app)



@app.route("/")
def home():
    city_01 = {
        "name" : "Tallinn",
        "descr" : "Capital",
        "bio" : "Tallinn is a great city!"
    }
    city_02 = {
        "name" : "Tartu",
        "descr" : "University city",
        "bio" : "Tartu is a small city."
    }
    cities = [city_01, city_02]
    return render_template('index.html', cities=cities)

# @app.route('/playing_around_with_databases')
# def playing_around_with_databases():
#     movies = mongo.db.movies.find()
#     return "This is where we will be playing around with databases"

# retrieves full recipe from database when a user clicks on'View Recipe' button

@app.route('/show_recipe/<recipe_id>')

def show_recipe(recipe_id):

    recipe_count =mongo.db.recipes.count()

    return render_template('showrecipe.html', recipe_count=recipe_count, recipe=mongo.db.recipes.find_one({'_id':ObjectId(recipe_id)}))

# @app.route("/europe")
# def europe():
#     return render_template("index.html")

# @app.route("/estonia")
# def estonia():
#     city_01 = {
#         "name" : "Tallinn",
#         "descr" : "Capital"
#     }
#     city_02 = {
#         "name" : "Tartu",
#         "descr" : "University city"
#     }
#     cities = [city_01, city_02]
#     return render_template("country.html", cities=cities)

# @app.route("/north-america")
# def america():
#     return "This is the north american home page"

# @app.route("/asia")
# def asia():
#     return "This is the asian home page"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
