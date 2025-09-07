function showAlert() {
  alert("Loading weather report...");
}

function acceptCookies() {
  document.getElementById("cookie").style.display = "none";
}

function convertTemps(select) {
  const isFahrenheit = select.value === "f";
  const highs = document.querySelectorAll(".high");
  const lows = document.querySelectorAll(".low");

  highs.forEach(span => {
    let temp = parseInt(span.textContent);
    span.textContent = isFahrenheit
      ? Math.round(temp * 9/5 + 32)
      : Math.round((temp - 32) * 5/9);
  });

  lows.forEach(span => {
    let temp = parseInt(span.textContent);
    span.textContent = isFahrenheit
      ? Math.round(temp * 9/5 + 32)
      : Math.round((temp - 32) * 5/9);
  });
}
