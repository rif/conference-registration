$(function(){
   $("#email").click(function(e){
       $("#email-response").fadeIn();
       var email_href = $(this).attr("href");
       $.get(email_href, function(response){
            $("#email-response").text(response);
        });
        e.preventDefault();
    });
});
