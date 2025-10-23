document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const user = document.getElementById("username").value;
  const pass = document.getElementById("password").value;
  const message = document.getElementById("message");

  // Usuario y contraseña de ejemplo
  const usuarioValido = "admin";
  const contraseñaValida = "1234";

  if (user === usuarioValido && pass === contraseñaValida) {
    message.style.color = "green";
    message.textContent = "¡Login exitoso! Redirigiendo...";
    setTimeout(() => {
      window.location.href = "bienvenido.html";
    }, 1500);
  } else {
    message.style.color = "red";
    message.textContent = "Usuario o contraseña incorrectos.";
  }
});
