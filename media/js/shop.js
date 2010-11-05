$(function(){
   $(".shop-row").hover(
      function () {
        $(this).css("font-size", "120%");
//         $(this).prev().css("font-size", "120%");
//         $(this).next().css("font-size", "120%");
        $(this).css("background", "#EEE");
        $("a.mmod,a.pmod", this).css("display", "inline")
      },
      function () {
        $(this).css("font-size", "100%");
//         $(this).prev().css("font-size", "100%");
//         $(this).next().css("font-size", "100%");
        $(this).css("background", "#FFF");
        $("a.mmod,a.pmod", this).css("display", "none")
      }
    );
   $("span.counter").each(function(){
       $(this).load($(this).attr("id"));
    });
   $("span.partsum").each(function(){
       $(this).load($(this).attr("id"));
    });
   $("#totsum").each(function(){
       $(this).load($(this).attr("class"));
    });
   $("a.mmod, a.pmod").click(function(e){
       var id = $(this).parents(".shop-row").attr("id");
       var post_url = $(this).attr("href");
       var partsum_element = $("#"+ id +" span.partsum");
       var totsum_element = $("#totsum");
       var operation = $(this).attr("class");
       if(operation == "mmod"){
           var counter_element = $(this).next(".counter");
           var value = -1;
        }
       if(operation == "pmod"){
           var counter_element = $(this).prev(".counter");
           var value = 1;
        }
       $.post(post_url, {csrfmiddlewaretoken:  $("input:first").val(),
                                item: id,
                                value: value}, function(response){
                                    counter_element.text(response);
                                    partsum_element.load(partsum_element.attr("id"));
                                    totsum_element.load(totsum_element.attr("class"));
                                });
       e.preventDefault();
    });
   $(".have_paper").each(function(){
        var parent = $(this).parents(".shop-row");
        var checkbox = $(this);
        var id = parent.attr("id");
        $.get($(this).attr('id'), function(result){
            if(result == "True") {
                var textbox = $(".paper_nb", parent);
                checkbox.attr('checked', true);
                $.get(textbox.attr('id'), function(result){
                    textbox.val(result);
                });
                $(".paper_nb_span", parent).show();
            } else {
                checkbox.attr('checked', false);
                $(".paper_nb_span", parent).hide();
            }
        });
   });
   $(".have_paper").click(function(){
        var checked = $(this).attr('checked');
        var parent = $(this).parents(".shop-row");
        var id = parent.attr("id");
        var partsum_element = $("#"+ id +" span.partsum");
        var totsum_element = $("#totsum");
        var item_price_span = $(".item_price", parent);
        post_url = item_price_span.attr("id");
        if(checked){
            var textbox = $(".paper_nb", parent);
            $.get(textbox.attr('id'), function(result){
                textbox.val(result);
            });
            $(".paper_nb_span", parent).fadeIn();
        } else {
            $(".paper_nb_span", parent).fadeOut();
        }
        $.post(post_url, {csrfmiddlewaretoken:  $("input:first").val(),
                            item: id,
                            value: checked}, function(response){
                                item_price_span.text(response);
                                partsum_element.load(partsum_element.attr("id"));
                                totsum_element.load(totsum_element.attr("class"));
                            });
   });
   $(".paper_nb").change(function(){
       var textbox = $(this);
       var parent = $(this).parents(".shop-row");
       var id = parent.attr("id");
       post_url = $(this).attr("href");
       $.post(post_url, {csrfmiddlewaretoken:  $("input:first").val(),
                            item: id,
                            value: textbox.val()}, function(response){
                                textbox.css("border", "2px dashed green");
                            });
   });
   $("#email").click(function(e){
       var email_href = $(this).attr("href");
       $.get(email_href, function(response){
            $("#email-response").text(response);
            $("#email-response").fadeIn("slow");
        });
        e.preventDefault();
    });
    $("#paypal-form").submit(function() {
        $("#paypal-div").load("/payment/paypal/", function(){
            $("#paypal-form", "#paypal-div").submit();
        });
        return false;
    });
});
