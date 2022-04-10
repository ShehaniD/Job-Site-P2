var validateForm = function () {
    console.log("validating form");
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
    var _a, _b, _c, _d, _e, _f, _g, _h;
    form_data_json = {
        fName: (_a = document.getElementById("firstName").value) !== null && _a !== void 0 ? _a : "",
        lName: (_b = document.getElementById("lastName").value) !== null && _b !== void 0 ? _b : "",
        email: (_c = document.getElementById("email").value) !== null && _c !== void 0 ? _c : "",
        address: (_d = document.getElementById("address").value) !== null && _d !== void 0 ? _d : "",
        address2: (_e = document.getElementById("address2").value) !== null && _e !== void 0 ? _e : "",
        country: (_f = document.getElementById("country").value) !== null && _f !== void 0 ? _f : "",
        state: (_g = document.getElementById("state").value) !== null && _g !== void 0 ? _g : "",
        zipcode: (_h = document.getElementById("zip").value) !== null && _h !== void 0 ? _h : "",
    };
    console.log(form_data_json);
};
