document.addEventListener("DOMContentLoaded", function () {
    const toc = document.querySelector("#toc");
    const headers = document.querySelectorAll(".card-body h3");
  
    headers.forEach((header, index) => {
      const id = `section-${index}`;
      header.id = id;
  
      const a = document.createElement("a");
      a.classList.add("nav-link");
      a.href = `#${id}`;
      a.textContent = header.textContent;
  
      toc.appendChild(a);
    });
  
    // Плавная прокрутка
    document.querySelectorAll("#toc a").forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
        e.preventDefault();
  
        document.querySelector(this.getAttribute("href")).scrollIntoView({
          behavior: "smooth",
        });
      });
    });
  });