# Cookbook-of-Marta

The aim of my project is to have a place to store my recipes and also enable the user to share their recepies there.
It is a very basic app that serves the purpose of giving as much information as possible about the recipe. 

----
## UX

The goal of the project is to be informative and easy to read. The home page has a modern looking layput with the materialize feature called parallax.

### User stories

* As a user I want to visit this site to have information about selected recepies. 
* As a user I want to know before trying to cook what is the type of this recipe (vegetarian or non-vegetarian).
* As a user I want to know before choosing what recipe to do what is the difficuly level. There are three levels: super easy, not too tricky, showing off.
* As a user I would want to add also my recipes there so next time I will do them I have them alreay stored and can easily look up on my phone the ingredients when being the store.
* As a user I want the webpage to load fast and give the  opportunity to easily go back to home page after visiting the add recipes and edit recipes pages.
----
## Wireframe

The wireframe for this project is under static folder in the wireframe folder.

----
## Features

* First feature is the read function. The user can see the whole recipe on the home page. 
* Second feature is to add a recipe to the library.
* Third feature is to edit the existing recipe
* Fourth feature is the update function to implement the changes for teh existing recipe.
* Fifth feature is to delete recipes. The user can delete recipes until there is 4 recipes left. It won't be possible to delete more recipes when there isonly four left. 
Clicking on the "Delete Recipe" button will result in a popup modal being dispalyed asking the user to confirm that they want to delete that particular recipe. 

* Features Left To Implement:
1. Implement parallax feature to make it easily scrollable and give modern looking.
2. Have the alert box when a recipe was successfully deleted.

----
## Technologies used

* [JavaScript](https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js)
JavaScript  syntax was used to add the buttons to add or remove ingredients on the add recipe and edit recipe pages.

* [CSS](https://www.w3schools.com/css/css_intro.asp)
I used CSS to style the header and footer of the templates.

* [Bootstrap v3.3.7](https://getbootstrap.com/docs/3.3/getting-started/#download) 
Bootstrap was used to give the project a simple and responsive layout.

* [JQuery](https://cdnjs.com/libraries/jquery/) To have the alert boxes when user tries to delete a recipe.

* [Materialize](https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js)
I used this framework to have styled icons.

* Flask was used to run the application and code was written in the Python.

* MongoDB Atlas was used for creating and storing the database.

* Jinja was used for rendering the templates.

* In this project I used different libraries: 
 [Bootstrap.CSS](https://getbootstrap.com),
 Bootstrap.js;
 Jquery.js.

----
## Testing

1.All HTML and CSS code used on the site has been tested using
[The W3 CSS Validation Service](https://jigsaw.w3.org/css-validator/) and
[The W3 Markup Validation Service](https://validator.w3.org/).
The W3C shows that we conform to the standards of HTML and CSS. 

2.Prototype code was written and tested using Gitpod and Chrome Developer Tools.

3.All Javascript and jQuery code on the website has been tested using [JSHint](https://jshint.com/).

4.Site was viewed and tested in Google Chrome, Mozilla Firefox and Internet Explorer.

----
## Deployment
 
The hosting platform for this site is Heroku. Here is the link for my site .  To deploy the application to Heroku,
 I created an app with a unique name and linked it to the relevant GitHub repository to allow for automatic deploys from the GitHub master branch. 
 I used the following command to create a file containing a list of the files that Heroku requires to run the application: sudo pip3 freeze --local > requirements 
 I also create a Procfile using the following command: echo web: python3 app.py > Procfile I then added, committed and pushed both of this files to Git Hub. I used 
 the settings tab in Heroku to set the IP address and Port as config variables.
 For production I also stored the MONGO URI string and DATABASE NAME as config variables and accessed them using the os.getenv() method and I set debug to False.

----
## Credits

The recepies I added to my mongodatabase i got [here](https://www.jamieoliver.com/recipes/category/dishtype/pasta-risotto/).

### Acknowledgements

I would like to thank my mentor Moosa Hassan for encouraging to do the recipes app and giving advice on it. A lot was made much more clearer to me
thanks to the stand up sessions with my tutor Xavier Astor from Code Institute. The biggest help to solve the problems while coding I got from
Code Institute tutor tab, where I had two screen sharing sessions.
The code to have the add and remove ingredients and also the alert boxe I got visiting this [site](http://online-cookbook4.herokuapp.com/edit_recipe/5de189ff2b8170000c9fcbe4).

----
