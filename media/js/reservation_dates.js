$(function(){
    $("#email").click(function(e){
       var email_href = $(this).attr("href");
       $.get(email_href, function(response){
            $("#email-response").text(response);
            $("#email-response").fadeIn("slow");
        });
        e.preventDefault();
    });
});
