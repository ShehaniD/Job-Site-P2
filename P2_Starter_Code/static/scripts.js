var validateForm = function () {
    console.log('validating form');
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll(".needs-validation");
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms).forEach(function (form) {
        form.addEventListener("submit", function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add("was-validated");
        }, false);
    });
};

var form_data_json = {};

var submitForm = function () {
    form_data_json = {
        fName: document.getElementById('firstName').value ?? "",
        lName: document.getElementById('lastName').value ?? "",
        email: document.getElementById('email').value ?? "",
        address: document.getElementById('address').value ?? "",
        address2: document.getElementById('address2').value ?? "",
        country: document.getElementById('country').value ?? "",
        state: document.getElementById('state').value ?? "",
        zipcode: document.getElementById('zip').value ?? ""
    }

    console.log(form_data_json);
}
