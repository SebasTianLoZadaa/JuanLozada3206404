const x = document.getElementById("demo");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(success, error);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function success(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}

function error() {
  alert("Sorry, no position available.");
}

function dragstartHandler(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function dragoverHandler(ev) {
  ev.preventDefault();
}

function dropHandler(ev) {
  ev.preventDefault();
  const data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));

}


document.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("banderaCanvas");
  if (!canvas) return; // por si no lo encuentra

  const ctx = canvas.getContext("2d");

  function dibujarBandera() {
    // Amarillo (arriba)
    ctx.fillStyle = "#FFD700";
    ctx.fillRect(0, 0, 400, 80);

    // Azul (centro)
    ctx.fillStyle = "#0033A0";
    ctx.fillRect(0, 80, 400, 80);

    // Rojo (abajo)
    ctx.fillStyle = "#CE1126";
    ctx.fillRect(0, 160, 400, 80);
  }

  canvas.addEventListener("click", dibujarBandera);
});

const playBtn = document.getElementById('playBtn');
  const audio = document.getElementById('audio');
  let isPlaying = false;

  playBtn.addEventListener('click', () => {
    if (!isPlaying) {
      audio.play();
      playBtn.textContent = "⏸️ Pausar";
      isPlaying = true;
    } else {
      audio.pause();
      playBtn.textContent = "🎶 Reproducir";
      isPlaying = false;
    }
  }); 