const authenticatedUser = document.getElementById("authenticatedUser");
const dropDownSection = document.querySelector(".dropDownSections");
const dropDown = document.querySelector(".dropDown");

authenticatedUser.addEventListener("click", () => {
  if (dropDownSection.style.display === "flex") {
    dropDownSection.style.display = "none";
  } else {
    dropDownSection.style.display = "flex";
  }
});
