$("form[name=signup_form]").submit(function(e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    console.log("data");
    console.log(data);

    $.ajax({
        url: "/user/signup",
        type: "POST",
        data: data,
        dataType: "json",
        success: function (response) {
            window.location.href = '/dashboard/';
        },
        error: function (response) {
            $error.text(response.responseJSON.error).removeClass('error--hidden');
        }
    });

    e.preventDefault();
});