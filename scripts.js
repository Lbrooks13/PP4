// JavaScript to control the popup form behavior

// Get elements
const bookTableBtn = document.getElementById('book-table-btn');
const popupForm = document.getElementById('popup-form');
const closeBtn = document.querySelector('.close-btn');

// Show the popup when "Book a Table" is clicked
bookTableBtn.addEventListener('click', function(event) {
  event.preventDefault();
  popupForm.style.display = 'flex';
});

// Hide the popup when the close button is clicked
closeBtn.addEventListener('click', function() {
  popupForm.style.display = 'none';
});

// Hide the popup if clicking outside the popup content
window.addEventListener('click', function(event) {
  if (event.target == popupForm) {
    popupForm.style.display = 'none';
  }
});

// Field Validation
function valForm() {
  const nameInput = document.getElementsById('name');

  if (!isNaN(nameInput)){
    alert("Please enter a name using alphabetic characters only")
    nameInput.value = "";
    return false;
  }
}

