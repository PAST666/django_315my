document.addEventListener("DOMContentLoaded", function () {
  var images = document.querySelectorAll("img");
  images.forEach(function (img) {
    img.classList.add("img-fluid");
  });
});
