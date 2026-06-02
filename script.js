async function loadBikes() {

    const res = await fetch("data.json");
    let bikes = await res.json();

    const carbonOnly =
        document.getElementById("carbonOnly").checked;

    if (carbonOnly) {
        bikes = bikes.filter(
            b => (b.frame || "").toLowerCase().includes("carbon")
        );
    }

    bikes.sort(
        (a, b) => (b.deal_score || 0) - (a.deal_score || 0)
    );

    document.getElementById("bikeCount").innerText =
        bikes.length;

    const avg =
        bikes.reduce((s, b) => s + (b.discount || 0), 0)
        / bikes.length;

    document.getElementById("avgDiscount").innerText =
        Math.round(avg) + "%";

    const table =
        document.getElementById("bikeTable");

    table.innerHTML = "";

    bikes.forEach(b => {

        table.innerHTML += `
            <tr>

                <td>
                    <span class="score">
                        ${b.deal_score || 0}
                    </span>
                </td>

                <td>
                    <a href="${b.url}" target="_blank">
                        ${b.model}
                    </a>
                </td>

                <td>${b.price} €</td>

                <td>${b.old_price || "-"} €</td>

                <td class="discount">
                    -${b.discount || 0}%
                </td>

                <td>${b.weight || "-"}</td>

                <td>${b.groupset || "-"}</td>

                <td>${b.dealer}</td>

            </tr>
        `;
    });

}

document
    .getElementById("carbonOnly")
    .addEventListener("change", loadBikes);

loadBikes();