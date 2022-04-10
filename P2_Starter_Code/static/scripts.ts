const validateForm = () => {
  console.log("validating form");
  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms).forEach((form: HTMLInputElement) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add("was-validated");
      },
      false
    );
  });
};

let form_data_json = {};

const submitForm = function () {
  form_data_json = {
    fName:
      (document.getElementById("firstName") as HTMLInputElement).value ?? "",
    lName:
      (document.getElementById("lastName") as HTMLInputElement).value ?? "",
    email: (document.getElementById("email") as HTMLInputElement).value ?? "",
    address:
      (document.getElementById("address") as HTMLInputElement).value ?? "",
    address2:
      (document.getElementById("address2") as HTMLInputElement).value ?? "",
    country:
      (document.getElementById("country") as HTMLInputElement).value ?? "",
    state: (document.getElementById("state") as HTMLInputElement).value ?? "",
    zipcode: (document.getElementById("zip") as HTMLInputElement).value ?? "",
  };

  console.log(form_data_json);
};
