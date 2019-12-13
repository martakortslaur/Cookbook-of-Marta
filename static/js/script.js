$(document).ready(function() {

    
    /* Dynamically add new ingredient input field in recipe forms*/

    $(".new-input-btn").on("click", function() {

        $('<input type="text" class="form-control recipe_ingredients" name="recipe_ingredients" id="ingredients-row"  required >').insertBefore(".new-input-btn");

    });

    /*removes last input element in ingredient list*/

    $(".remove-input-btn").on("click", function() {

        $("#ingredients-row input:last").remove();

    });


});