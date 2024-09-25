// Nav Bar
const toggleBtn = document.querySelector('.menu');
const toggleBtnIcon = toggleBtn.querySelector('i');
const dropDownMenu = document.querySelector('.dropdown-menu');

toggleBtn.onclick = function () {
  dropDownMenu.classList.toggle('open');
  const isOpen = dropDownMenu.classList.contains('open');
  toggleBtnIcon.classList.toggle('fa-bars', !isOpen);
  toggleBtnIcon.classList.toggle('fa-xmark', isOpen);
};

// Modal and Get Started Button
var modal = document.getElementById("myModal");
var btn = document.getElementById("openModal");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
  modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Handle modal button clicks
document.getElementById("studentBtn").onclick = function() {
    
    window.location.href = 'student_login.html'; // Redirect to student login
    modal.style.display = "none";
}

document.getElementById("merchantBtn").onclick = function() {
    alert("You selected MERCHANT!");
    window.location.href = 'merchant_login.html'; // Redirect to merchant login
    modal.style.display = "none";
}

// Student and Merchant login handling
document.getElementById('studentLoginForm')?.addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Logged in as Student!');
    // Perform login logic here
    window.location.href = 'student_dashboard.html'; // Redirect to student dashboard
});

document.getElementById('merchantLoginForm')?.addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Logged in as Merchant!');
    // Perform login logic here
    window.location.href = 'merchant_dashboard.html'; // Redirect to merchant dashboard
});

// Google login handling
document.getElementById('googleLoginBtn')?.addEventListener('click', function() {
    alert('Google Login not implemented.');
    // Add Google login logic here
});

// Sign Up handling
document.getElementById('signUpBtn')?.addEventListener('click', function() {
    alert('Redirecting to Student Sign Up!');
    window.location.href = 'signup.html'; // Redirect to sign-up page
});

document.getElementById('merchantSignUpBtn')?.addEventListener('click', function() {
    alert('Redirecting to Merchant Sign Up!');
    window.location.href = 'merchant_signup.html'; // Redirect to merchant sign-up page
});
function handleEmailLogin() {
  var email = document.getElementById('email').value;
  var password = document.getElementById('password').value;

  if (!email || !password) {
      alert('Please fill in both fields.');
      return;
  }

  // Authentication logic goes here

  // For now, we'll assume authentication is successful
  alert('Logging in with Email: ' + email);

  // Redirect to student dashboard
  window.location.href = 'student_dashboard.html';
}

