async function loadBikes() {
    const res = await fetch('data.json');
    let bikes = await res.json();

    const carbonKeywords = ["carbon", "cf", "c:62", "cfr", "slr", "advanced"];

    const onlyCarbon = document.getElementById("carbonOnly").checked;

    if (onlyCarbon) {
        bikes = bikes.filter(b =>
            carbonKeywords.some(k =>
                (b.frame || "").toLowerCase().includes(k)
            )
        );
    }

    const container = document.getElementById("bikes");
    container.innerHTML = "";

    bikes.forEach(b => {
        container.innerHTML += `
            <div class="bike">
                <h3>${b.model}</h3>
                <p>${b.dealer}</p>
                <p>${b.price} €</p>
                <a href="${b.url}" target="_blank">Zum Angebot</a>
            </div>
        `;
    });
}

document.getElementById("carbonOnly").addEventListener("change", loadBikes);
loadBikes();