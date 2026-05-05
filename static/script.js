function moveButton() {
    const button = document.querySelector(".no");

    const x = Math.random() * 300 - 150;
    const y = Math.random() * 300 - 150;

    button.style.transform = `translate(${x}px, ${y}px)`;
}