//Query All input fields
var form_fields = document.getElementsByTagName('input')
form_fields[1].placeholder = 'Username..';
form_fields[2].placeholder = 'Email..';
form_fields[3].placeholder = 'Enter password...';
form_fields[4].placeholder = 'Re-enter Password...';


for (var field in form_fields) {
    form_fields[field].className += ' form-control'
}

$("#id_email").on("blur", function (e) {
    var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (mailformat.test(String($("#id_email").val()))) {
        //alert("Valid email address!");
        $("#id_email").focus();
        console.log("valid email");
        emailChecker();
        return true;
    }
    else {
        alert("You have entered an invalid email address!");
        $("#id_email").focus();
        return false;
    }
})

function emailChecker() {

    var email = $('#id_email').val();
    $.ajax({
        url: "{% url 'socialapp:emailduplicationcheck' email %}",
        method: 'GET',
        data: { email: email },
        dataType: 'json',
        // success:(function (response) { // on success
        // 	console.log("email exists", response['status'])
        // 	console.log(typeof response);
        // }) ,
        // error:(function (error) { // on success
        // 	console.log("error", error)
        // })
    })
        .done(function (response) { // on success
            // var obj = JSON.parse(response);
            console.log("=email exists",response.status)
        })
        .fail(function (xhr, errmsg, err) { // on error
            console.log("email not exist")

            console.log(errmsg);
        });
}