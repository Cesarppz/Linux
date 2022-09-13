$(document).ready(function(){
    function ajax_login(){
        $.ajax({
            url: '/ajax-login',
            data: $('form').serialize(),
            type: 'POST',
            datatype: 'json',
            success:function(response){
                console.log('Bien hecho');
                console.log(response);
            },
            error:function(error){
                console.log('Mal hecho');
                console.log(error);
            }
        });
    }

    $('#login-form').submit(function(event) {
        event.preventDefault();
        ajax_login();
    });
});