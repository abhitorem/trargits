document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".card").forEach((card, index) => {
    card.style.opacity = "0";
    card.style.transform = "translateY(12px)";
    setTimeout(() => {
      card.style.transition = "all 380ms ease";
      card.style.opacity = "1";
      card.style.transform = "translateY(0)";
    }, index * 90);
  });
});
