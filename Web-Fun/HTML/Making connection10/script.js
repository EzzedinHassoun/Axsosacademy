function editProfile() {
  const nameElement = document.getElementById("name");
  const newName = prompt("Enter your new name:");
  if (newName) {
    nameElement.textContent = newName;
  }
}

function handleRequest(icon, name = null, avatar = null) {
  const listItem = icon.closest(".card-list-item");
  if (listItem) {
    listItem.remove();

    const requestCount = document.handleRequest("request-count");
    let count = parseInt(requestCount.textContent);
    requestCount.textContent = count > 0 ? count - 1 : 0;

    if (icon.alt === "accept" && name && avatar) {
      const connectionList = document.handleRequest("connection-list");
      const newConnection = document.createElement("li");

    }
  }
}