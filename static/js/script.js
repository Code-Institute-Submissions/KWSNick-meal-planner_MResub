 $(document).ready(function(){
    // Materialize initialisation and options
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.collapsible').collapsible();
    $('.fixed-action-btn').floatingActionButton({
        direction: 'left'
    });
    $('.tooltipped').tooltip();
    $('.modal').modal({
        preventScrolling: false,
        endingTop: '20%',
    });
    // Calculate minimum height for the main content section to prevent the footer not being at the bottom of the screen
    let minHeight = $(window).height() - ($('nav').height() + $('footer').height());
    $('.main_content').css('min-height', minHeight);
    // Script to check the entered passwords in registration are the same and alert the user if they are not. 
    $('#confirm_password').focusout(function passwordValidate(){
        let pwd1 = $('#password').val();
        let pwd2 = $('#confirm_password').val();
        if (pwd1 != pwd2) {
                $('#pwd_no_match').remove();
                $('#password_confirmation').append('<span id="pwd_no_match" class="form_tip form_alert">PASSWORDS DO NOT MATCH</span>');
                $('#confirm_password').removeClass('valid');
                $('#password, #confirm_password').addClass('invalid');
        } else {
            $('#pwd_no_match').remove();
            $('#password, #confirm_password').removeClass('invalid');
        }
    })
    // Checks if all registration fields have valid class assigned and provides submit button if true. Otherwise removes the submit button.
    $('#registration_form div div input').focusout(function deployRegBtn(){
        if ($('#first_name').hasClass('valid') && $('#last_name').hasClass('valid') && $('#username').hasClass('valid') && $('#password').hasClass('valid') && $('#confirm_password').hasClass('valid')) {
            $('#register').removeClass("disabled");
        } else {
           $('#register').addClass("disabled");
        }           
    })
    // Checks if all login fields have valid class assigned and provides submit button if true. Otherwise removes the submit button.
    $('#login_form div div input').focusout(function deployLoginBtn(){
        if ($('#username').hasClass('valid') && $('#password').hasClass('valid')) {
            $('#login_btn').removeClass("disabled");
        } else {
           $('#login_btn').addClass("disabled");
        }           
    })
    // Function that adds a new input row beneath clicked button for shared with section of form
    $('#sharing').on('click', 'button', function(){
        button = $(this).attr('id');
        function addShare(){
            i = $('.add_share').length;
            j = i + 1;
            $(`#`+button).after(`<input class="center shared_with add_share" id="shared_with`+[j]+`" name="shared_with`+[j]+`" type="text"><label for="shared_with`+[j]+`">Shared With</label><button id="button`+[j]+`" type="button" class="hoverable right btn-floating btn-small waves-effect waves-light red"><i class="fas fa-plus"></i></button>`);
        }
        addShare();
        $(`#`+button).hide();
    })
    // Function that adds a new input row beneath clicked button for ingredients section of form
    $('#ingredients_list').on('click', 'button', function(){
        button = $(this).attr('id');
        function addIng(){
            i = $('.add_ingredient').length;
            j = i + 1;
            $(`#`+button).after(`<div class="row">
                    <div class="input-field col s6">
                        <input class="center add_ingredient" id="ingredient_name`+[j]+`" name="ingredient_name`+[j]+`" type="text">
                        <label for="ingredient_name`+[j]+`">Ingredient</label>
                    </div>
                    <div class="input-field col s3">
                        <input class="center" id="ingredient_quantity`+[j]+`" name="ingredient_quantity`+[j]+`" type="number" step="0.01">
                        <label for="ingredient_quantity`+[j]+`">Quantity</label>
                    </div>
                    <div class="input-field col s3">
                        <label for="ingredient_unit`+[j]+`" class="hide">Unit</label>
                        <select class="center" id="ingredient_unit`+[j]+`" name="ingredient_unit`+[j]+`">
                            <option value="None">Unit</option>
                            <option value="grams">Grams</option>
                            <option value="ml">ml</option>
                            <option value="quantity">Quantity</option>   
                        </select>
                    </div>
                </div>
                <button id="ing_button`+[j]+`" type="button" class="hoverable btn-floating btn-small waves-effect waves-light red"><i class="fas fa-plus"></i></button>`);
            $('select').formSelect();
            }
        addIng();
        $(`#`+button).hide();
    })
    // Function that adds a new input row beneath clicked button for method section of form
    $('#step_list').on('click', 'button', function(){
        button = $(this).attr('id');
        console.log(button);
        function addStep(){
            i = $('.add_step').length;
            j = i + 1;
            $(`#`+button).after(`<div class="row">
                    <div class="col s1">
                        <p class="step-no">`+[j]+`.</p>
                    </div>
                    <div class="col s11 input-field">
                        <input class="center add_step" id="step`+[j]+`" name="step`+[j]+`" type="text">
                        <label for="step`+[j]+`">Step</label>
                    </div>
                </div>
                <button id="step_button`+[j]+`" type="button" class="hoverable right btn-floating btn-small waves-effect waves-light red"><i class="fas fa-plus"></i></button>`)
            }
        addStep();
        $(`#`+button).hide();
    })
    // Function to check if the image url has changed, and if it has to load the image using ajax
    $('#image_url').change(function(){
        $.ajax({url: "", success: function(){
            image = $('#image_url').val();
            $('#image_preview').remove();
            $('#image_placeholder').remove();
            if (image == ""){
                 $('#image_preview').remove();
                 $('#image_url').parent().siblings().after(`<img id="image_placeholder" class="recipe_image" src="../static/images/recipe_img_pholder.png" alt="recipe image placeholder">`);
                 ('#image_url').val("../static/images/recipe_img_pholder.png")
                 $('#image_description').val("recipe image placeholder")
            }
            else {
                $('#image_url').parent().siblings().after(`<img id="image_preview" class="recipe_image" src="`+image+`" alt="recipe image preview">`);
            }
        }});
    })
  });