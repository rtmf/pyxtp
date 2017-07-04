  
  $(document).ready(function() {
  //$(function() {
    $('.error').hide();
    $(".cbp-mc-submit").click(function() {
      // validate and process form here
      
    $('.error').hide();
  	var name = $("input#nomeinput").val();
	//if name is empty
    if (name == "") {
		$("label#name_error").show();
		$("input#nomeinput").focus();
		return false;
    }
        
  	var email = $("input#emailinput").val();
	  
    if (email == "") {
        $("label#email_error").show();
        $("input#emailinput").focus();
        return false;
    }else {
        if ((!isValidEmailAddress(email)) || (email).indexOf('.') == -1 || (email).indexOf('@') == -1 || !getLen(email) ){
			$("label#email_valid").show();
            $("input#emailinput").focus();
            return false;
        }
    }
	  
	var msg = $("textarea#msginput").val();
	  
	var check = $("input#checkinput").val();
	    if (check != "") {
        $("label#trick_error").show();
        $("input#checkinput").focus();
        return false;
    }
	  
  	
	  
	  
	// AJAX CALL THE PHP FILE ( before the button click function is closed)
	  
		var dataString = 'name='+ name + '&email=' + email + '&msg=' + msg; //or body insted of msg
		  //alert (dataString);return false;
		  $.ajax({
			type: "POST",
			url: "js/send-form.php",
			data: dataString,
			success: function() {
				$('#contact_form').html("<div style='height:380px;' id='message'></div>");
				$('#message').html("<h2>Contact Form Submitted!</h2>")
				.append("<p>We will be in touch soon.</p>")
				.hide()
				.fadeIn(1500, function() {
					$('#message').show();
				});
			}
		  });
		  return false;
	  
	// AJAX CALL THE PHP FILE end
	
	
	
	//############################  functions   //############################
	
    function isValidEmailAddress(emailAddress) {
        var pattern = new RegExp(/^(("[\w-+\s]+")|([\w-+]+(?:\.[\w-+]+)*)|("[\w-+\s]+")([\w-+]+(?:\.[\w-+]+)*))(@((?:[\w-+]+\.)*\w[\w-+]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][\d]\.|1[\d]{2}\.|[\d]{1,2}\.))((25[0-5]|2[0-4][\d]|1[\d]{2}|[\d]{1,2})\.){2}(25[0-5]|2[0-4][\d]|1[\d]{2}|[\d]{1,2})\]?$)/i);
        console.log(pattern.test(emailAddress));
        return pattern.test(emailAddress);
    };
		
		
	//email structure namemail@site.tld  e.i. aa@bbb.it
    function getLen(emailAddress) {
						
        var atEmail = emailAddress.indexOf('@');
		var dotEmail = emailAddress.lastIndexOf('.');
		var nameEmail = emailAddress.substring(0, atEmail);
		var nameEmailLen = nameEmail.length;
		var siteLen = dotEmail-atEmail-1;
		
		if (nameEmailLen >=2 && siteLen >2 ){
			console.log('lungo ok');
			return true;
		}else {
			console.log('corto stop');
			return false;
			}
		   
    };
		
    }); // click function END
	
  });