document.querySelector('.menu-btn').addEventListener('click', () => {
  document.querySelector('.nav-menu').classList.toggle('show');
});
ScrollReveal().reveal('.showcase',{delay: 500});
ScrollReveal().reveal('.news-card', {delay: 500});
