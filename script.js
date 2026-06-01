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
    container.innerHTML += `
<div class="bike">
    <h3>${b.model}</h3>

    <p><b>Händler:</b> ${b.dealer}</p>
    <p><b>Kategorie:</b> ${b.category}</p>
    <p><b>Rahmen:</b> ${b.frame}</p>
    <p><b>Schaltung:</b> ${b.groupset}</p>
    <p><b>Gewicht:</b> ${b.weight}</p>
    <p><b>Laufräder:</b> ${b.wheelset}</p>

    <p>
      <b>${b.price} €</b>
      statt ${b.old_price} €
      (-${b.discount}%)
    </p>

    <p><b>Größen:</b> ${b.sizes.join(", ")}</p>

    <a href="${b.url}" target="_blank">
      Zum Angebot
    </a>
</div>
`;
        `;
    });
}

document.getElementById("carbonOnly").addEventListener("change", loadBikes);
loadBikes();