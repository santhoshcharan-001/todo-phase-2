$("#re-password").on("keyup",function(){
    var password = $("#password-register").val();
    var re_password = $("#re-password").val();
    console.log(password);
    console.log(re_password);
    if(password != re_password){
        // $("#re-password").val("");
        console.log("not matched")
        $(".details.nomargin").find("p").text("Passwords doesn't match.");
        $(".details.nomargin").find("p").css("color","red");
    }
    else
    {
        if(password=="")
        {
            $(".details.nomargin").find("p").text("Password cannot be empty.");
            $(".details.nomargin").find("p").css("color","red");
        }
        else{
            console.log("matched")
            $(".details.nomargin").find("p").text("Passwords matched.");
            $(".details.nomargin").find("p").css("color","green");
        }

    }
});


$("#username-register").on("keyup",function(){
    var username = $("#username-register").val();
    if(username=="")
    {
        $(".details.nouser").find("p").text("Username is required.");
        $(".details.nouser").find("p").css("color","red");
    }
    else{
        $.ajax({
            type: "get",
            url: "/check_username/?username="+username,
            success: function (response) {
                console.log(response);
                if(response.status=="Username already taken")
                {
                    $(".details.nouser").find("p").text("Username already taken.");
                    $(".details.nouser").find("p").css("color","red");
                }
                else{
                    $(".details.nouser").find("p").text("Username is available.");
                    $(".details.nouser").find("p").css("color","green");
                }
            }
        });
    }
});

$("#register-button").on("click",function(event){
    event.preventDefault();
    var username = $("#username-register").val();
    var password = $("#password-register").val();
    var re_password = $("#re-password").val();
    var username = $("#username-register").val();
    if(username=="")
    {
        $(".details.nouser").find("p").text("Username is required.");
        $(".details.nouser").find("p").css("color","red");
    }
    else{
        $.ajax({
            type: "get",
            url: "/check_username/?username="+username,
            success: function (response) {
                console.log(response);
                if(response.status=="Username already taken")
                {
                    $(".details.nouser").find("p").text("Username already taken.");
                    $(".details.nouser").find("p").css("color","red");
                }
                else{
                    $(".details.nouser").find("p").text("Username is available.");
                    $(".details.nouser").find("p").css("color","green");
                    if(password==re_password)
                    {
                        if(password=="")
                        {
                            $(".details.nomargin").find("p").text("Password cannot be empty.");
                            $(".details.nomargin").find("p").css("color","red");
                        }
                        else{
                            console.log("matched")
                            $(".details.nomargin").find("p").text("Passwords matched.");
                            $(".details.nomargin").find("p").css("color","green");
                            $("#register-form").submit();
                        }
                    }
                }
            }
        });
    }
});
// $(window).on("load", function () {
//     main();
//     console.log("loaded");
//   });
var options=$(".option");
console.log(options.first());

// onclick function


options.first().on("click", function () {
    console.log("login");
    if($(".login").hasClass("hide"))
    {
        $(".login").removeClass("hide");
    }
    if($(".register").hasClass("hide"))
    {
        console.log("okay");

    }
    else{
        $(".register").addClass("hide");
    }
});
$(".option").last().on("click",function(){
    console.log("register");
    if($(".register").hasClass("hide"))
    {
        $(".register").removeClass("hide");
    }
    if($(".login").hasClass("hide"))
    {
        console.log("okay");
       
    }
    else{
        $(".login").addClass("hide");
    }
});