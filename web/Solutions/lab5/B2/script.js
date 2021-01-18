function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}
function validateForm() {
    var check = true;

    var fname = document.forms['myForm']['fname'].value;
    var lname = document.forms['myForm']["lname"].value;
    var pass = document.forms['myForm']["pass"].value;
    if (
        (fname.length < 2 || fname.length > 30) ||
        (lname.length < 2 || lname.length > 30) ||
        (pass.length < 2 || pass.length > 30)  
    )
        check = false;

    var email = document.forms['myForm']['email'].value;
    if (!validateEmail(email))
        check = false;

    


    if (!check)
        alert("Invalid information!");
    else        
        alert("Complete!");
}

function resetAll() {
    document.forms['myForm'].reset();
}