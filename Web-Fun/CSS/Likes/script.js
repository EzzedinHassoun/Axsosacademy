document.querySelectorAll('.like-btn').forEach(button => {
  button.addEventListener('click', () => {
    const likesSpan = button.previousElementSibling.querySelector('.likes');
    let currentLikes = parseInt(likesSpan.textContent);
    likesSpan.textContent = currentLikes + 1;
  });
});
