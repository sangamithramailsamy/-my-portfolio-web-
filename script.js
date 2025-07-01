function showMessage() {
  alert("Welcome to Suguna Boutique! Browse our latest collections.");
}

document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault();
  alert(
    "Thank you for contacting Suguna Boutique! We will get back to you soon."
  );
  this.reset();
});
