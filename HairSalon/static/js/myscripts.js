document.addEventListener("DOMContentLoaded", function () {
  selectElement = document.getElementById("user_type");
  specialityInput = document.getElementById("speciality");

  selectElement.addEventListener("change", function () {
    if (selectElement.value === "client") {
      specialityInput.classList.add("hidden");
      specialityInput.value = "Not Applicable";
    } else if (selectElement.value === "professional") {
      specialityInput.classList.remove("hidden");
      specialityInput.value = "";
    } else if (selectElement.value === "user") {
      specialityInput.classList.add("hidden");
      specialityInput.value = "admin user stuff";
    } else if (selectElement.value === "appoint") {
      specialityInput.classList.add("hidden");
      specialityInput.value = "admin appoint stuff";
    }

    function ConfirmAction() {
      let answer = confirm('Are you sure you want to delete?');
      return answer
    }
  });
});




