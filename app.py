import os
from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId  


from os import path
if path.exists('env.py'):
    import env 

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'cookbook_database'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template('recipes.html', recipes=recipes)


@app.route('/add_recipe')
def add_recipe():
    types = mongo.db.types.find()
    difficulty = mongo.db.difficulty.find()

    return render_template('addrecipe.html', types=types, difficulty=difficulty)



@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
  
    recipes = mongo.db.recipes
    recipes.insert_one({
            'name' : request.form.get('recipe_name'),
            'description' : request.form.get('recipe_description'),
            'type' : request.form.get('recipe_type'),
            'difficulty' : request.form.get('recipe_difficulty'),
            'time' : request.form.get('recipe_time'),
            'ingredients' : request.form.getlist('recipe_ingredients'),
            'method' : request.form.get('recipe_method'),
            'tips' : request.form.get('recipe_tips'),
        })

    return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    types = mongo.db.types.find()
    difficulty = mongo.db.difficulty.find()
    dishes = mongo.db.recipes.find()
    recipe_count = mongo.db.recipes.count()
    recipe = mongo.db.recipes.find_one({'_id':ObjectId(recipe_id)})
    return render_template("editrecipe.html", recipe=recipe, dishes=dishes, types=types, difficulty=difficulty)
   

@app.route('/update_recipe/<recipe_id>', methods=["GET", "POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
    {
            'name' : request.form.get('recipe_name'),
            'description' : request.form.get('recipe_description'),
            'type' : request.form.get('recipe_type'),
            'difficulty' : request.form.get('recipe_difficulty'),
            'time' : request.form.get('recipe_time'),
            'ingredients' : request.form.getlist('recipe_ingredients'),
            'method' : request.form.get('recipe_method'),
            'tips' : request.form.get('recipe_tips'),
    })

    return redirect(url_for('get_recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
