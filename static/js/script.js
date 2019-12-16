$(document).ready(function() {

       /*Collaspes navbar when a link is clicked*/
    $(".navbar-nav").click(function() {
        $(".navbar-collapse").collapse("toggle");
    });

    
    /* Dynamically add new ingredient input field in recipe forms*/

    $(".new-input-btn").on("click", function() {

        $('<input type="text" class="form-control ingredients" name="ingredients" id="ingredients" placeholder="3 eggs" required >').insertBefore(".new-input-btn");

    });

    /*removes last input element in ingredient list*/

    $(".remove-input-btn").on("click", function() {

        $("#ingredients-row input:last").remove();

    });

    /* instantiate parallax*/
   
    //   $('.parallax').parallax();

        
});