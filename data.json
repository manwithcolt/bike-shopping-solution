let currentSort = "deal_score";

async function loadBikes() {

    const res = await fetch("data.json");
    let bikes = await res.json();

    const carbonOnly =
        document.getElementById("carbonOnly").checked;

    const gravelOnly =
        document.getElementById("gravelOnly").checked;

    const maxPrice =
        parseInt(
            document.getElementById("maxPrice").value
        ) || 999999;

    if (carbonOnly) {

        bikes = bikes.filter(
            b => (b.frame || "")
                .toLowerCase()
                .includes("carbon")
        );
    }

    if (gravelOnly) {

        bikes = bikes.filter(
            b => (b.category || "")
                .toLowerCase()
                .includes("gravel")
        );
    }

    bikes = bikes.filter(
        b => (b.price || 0) <= maxPrice
    );

    bikes.sort(
        (a, b) =>
            (b.deal_score || 0) -
            (a.deal_score || 0)
    );

    document.getElementById("bikeCount").innerText =
        bikes.length;

    if (bikes.length > 0) {

        const avg =
            bikes.reduce(
                (s, b) => s + (b.discount || 0),
                0
            ) / bikes.length;

        document.getElementById("avgDiscount").innerText =
            Math.round(avg) + "%";
    }

    const container =
        document.getElementById("bikeCards");

    container.innerHTML = "";

    bikes.forEach(b => {

        let scoreClass = "score-yellow";

        if ((b.deal_score || 0) >= 95)
            scoreClass = "score-red";
        else if ((b.deal_score || 0) >= 85)
            scoreClass = "score-green";

        let badges = "";

        if (b.is_new)
            badges += `<span class="badge-new">🆕 NEU</span>`;

        if (b.price_dropped)
            badges += `<span class="badge-price">📉 PREIS GEFALLEN</span>`;

        if ((b.deal_score || 0) >= 95)
            badges += `<span class="badge-deal">🔥 BEST DEAL</span>`;

        container.innerHTML += `

        <div class="bike-card">

            <div class="card-top">

                <span class="score ${scoreClass}">
                    ${b.deal_score}
                </span>

                <div class="badges">
                    ${badges}
                </div>

            </div>

            <div class="model">
                ${b.model}
            </div>

            <div class="price">
                ${b.price} €
            </div>

            <div class="old-price">
                statt ${b.old_price} €
            </div>

            <div class="discount">
                -${b.discount}%
            </div>

            <div class="details">
                <div>⚖️ ${b.weight}</div>
                <div>⚙️ ${b.groupset}</div>
                <div>🏪 ${b.dealer}</div>
                <div>📅 Seit ${b.first_seen || "-"}</div>
            </div>

            <a
                class="buy-button"
                href="${b.url}"
                target="_blank">
                Zum Angebot
            </a>

        </div>
        `;
    });
}

document
    .getElementById("carbonOnly")
    .addEventListener("change", loadBikes);

document
    .getElementById("gravelOnly")
    .addEventListener("change", loadBikes);

document
    .getElementById("maxPrice")
    .addEventListener("input", loadBikes);

loadBikes();