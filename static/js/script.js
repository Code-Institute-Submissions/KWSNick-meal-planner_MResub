 $(document).ready(function(){
    $('.sidenav').sidenav();
     $('select').formSelect();
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
    // Checks if all fields have valid class assigned and provides submit button if true. Otherwise removes the submit button.
    $('#registration_form div div input').focusout(function deployRegBtn(){
        if ($('#first_name').hasClass('valid')) {
            if ($('#last_name').hasClass('valid')) {
                if ($('#username').hasClass('valid')) {
                    if ($('#password').hasClass('valid')) {
                        if ($('#confirm_password').hasClass('valid')) {
                            $('#register').remove();
                            $('#register_button').append('<button id="register"class="col s2 center offset-s5 waves-effect waves-light btn-large green lighten-1" type="submit">Register</button>');
                        } else {
                            $('#register').remove();
                        }
                    } else {
                        $('#register').remove();
                    }
                } else {
                    $('#register').remove();
                }
            } else {
                $('#register').remove();
            }
        } else {
            $('#register').remove();
        }
    })
    $('#sharing').on('click', 'button', function(){
        button = $(this).attr('id');
        function addShare(){
            i = $('.add_share').length;
            j = i + 1;
            $(`#`+button).after(`<input class="center shared_with" id="shared_with`+[j]+`" name="shared_with`+[j]+`" type="text"><label for="shared_with`+[j]+`">Shared With</label><button id="button`+[j]+`" type="button" class="btn-floating btn-small waves-effect waves-light red add_share"><i class="fas fa-plus"></i></button>`);
        }
        addShare();
    })
  });