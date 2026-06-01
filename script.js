async function loadBikes() {
    const res = await fetch('data.json');
    let bikes = await res.json();

    const carbonKeywords = [
        "carbon",
        "cf",
        "c:62",
        "cfr",
        "slr",
        "advanced"
    ];

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

        const oldPrice = b.old_price
            ? `${b.old_price} €`
            : "-";

        const discount = b.discount
            ? `(-${b.discount}%)`
            : "";

        const sizes = Array.isArray(b.sizes)
            ? b.sizes.join(", ")
            : "-";

        container.innerHTML += `
            <div class="bike">

                <h2>${b.model || "-"}</h2>

                <p><strong>Händler:</strong> ${b.dealer || "-"}</p>

                <p><strong>Kategorie:</strong> ${b.category || "-"}</p>

                <p><strong>Rahmen:</strong> ${b.frame || "-"}</p>

                <p><strong>Schaltung:</strong> ${b.groupset || "-"}</p>

                <p><strong>Gewicht:</strong> ${b.weight || "-"}</p>

                <p><strong>Laufräder:</strong> ${b.wheelset || "-"}</p>

                <p>
                    <strong>Preis:</strong>
                    ${b.price || "-"} €
                </p>

                <p>
                    <strong>Vorher:</strong>
                    ${oldPrice}
                    ${discount}
                </p>

                <p>
                    <strong>Größen:</strong>
                    ${sizes}
                </p>

                <p>
                    <a href="${b.url}" target="_blank">
                        Zum Angebot
                    </a>
                </p>

            </div>
        `;
    });
}

document
    .getElementById("carbonOnly")
    .addEventListener("change", loadBikes);

loadBikes();