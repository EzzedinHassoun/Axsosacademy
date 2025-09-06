// Select all preview containers
const previews = document.querySelectorAll(".preview-container");

previews.forEach(container => {
  const video = container.querySelector("video");
  const icon = container.querySelector(".play-icon");

  // Play video + hide icon on hover
  video.addEventListener("mouseover", () => {
    video.play();
    icon.style.opacity = "0"; // hide
  });

  // Pause + reset video + show icon on mouseout
  video.addEventListener("mouseout", () => {
    video.pause();
    video.currentTime = 0;
    icon.style.opacity = "1"; // show again
  });
});
loginBtn.addEventListener("click", () => {
  if (loginBtn.textContent === "Login") {
    loginBtn.textContent = "Logout";
  } else {
    loginBtn.textContent = "Login";
  }
});

