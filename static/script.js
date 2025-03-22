document.addEventListener("DOMContentLoaded", function () {
    fetch("/timeline")
        .then(response => response.json())
        .then(data => {
            new TL.Timeline("timeline-embed", data);
        })
        .catch(error => console.error("Erro ao carregar timeline:", error));
});
