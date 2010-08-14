function reg_stat() {
    $('#login-form form').submit( function (event){
        event.preventDefault();
        $.post('/signup', $(this).serialize(), 
               function(data){
                   $('#login-form form').remove();
                   $('#login-form h1').replaceWith(data)
                   $("#login-form h1:contains('successfully')").each(
                       function() {
                           setTimeout(function() {
                               document.location = "/";
                           }, 1);           
                       });
               }, 'html');
    });
}


$(document).ready( function() {

    $('#login').click( function(event) {

        $('#login-form').html('&nbsp;').load("/login");
        event.preventDefault();

	$('#login-form').dialog({
	    autoOpen: true,
	    height: 300,
	    width: 350,
	    modal: true,
	    buttons: {
		'Login': function() {

                    $.post('/login', $('#f_login').serialize(), function (data) {
                        $('#useractions').html(data);
                    });
                    $(this).dialog('close');
		},
                Cancel: function() {
		    $(this).dialog('close');
		}
	    },
	    close: function() {
		$(this).dialog('close')
	    }
	});
    });


    $('#logout').click( function(event) {
        $('html').html().load("/logout" );
        
    });  


    $('#signup').click( function(event) {
        $('#login-form').html( '&nbsp;' ).load("/signup" );
        event.preventDefault(); 
	$('#login-form').dialog({
	    autoOpen: true,
	    height: 300,
	    width: 350,
	    modal: true,
	    buttons: {
		'Signup': function() {
                    $.post('/signup', $('#f_signup').serialize(), function (data) {
                        $('#useractions').html(data);
                    });
                    $(this).dialog('close');
		},
                Cancel: function() {
		    $(this).dialog('close');
		}
	    },
	    close: function() {
		$(this).dialog('close')
	    }
	});
    });

});
