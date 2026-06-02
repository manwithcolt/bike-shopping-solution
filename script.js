let currentSort = "deal_score";

async function loadBikes() {

    const res = await fetch("data.json");
    let bikes = await res.json();

    const carbonOnly =
        document.getElementById("carbonOnly").checked;

    if (carbonOnly) {
        bikes = bikes.filter(
            b => (b.frame || "")
                .toLowerCase()
                .includes("carbon")
        );
    }

    bikes.sort((a, b) => {

        if (currentSort === "weight") {

            const wa = parseFloat(
                (a.weight || "999")
                    .replace(" kg", "")
            );

            const wb = parseFloat(
                (b.weight || "999")
                    .replace(" kg", "")
            );

            return wa - wb;
        }

        return (b[currentSort] || 0)
            - (a[currentSort] || 0);

    });

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

    } else {

        document.getElementById("avgDiscount").innerText =
            "0%";

    }

    const table =
        document.getElementById("bikeTable");

    table.innerHTML = "";

    bikes.forEach(b => {

        let scoreClass = "score-yellow";

        if ((b.deal_score || 0) >= 95) {
            scoreClass = "score-red";
        }
        else if ((b.deal_score || 0) >= 85) {
            scoreClass = "score-green";
        }

        table.innerHTML += `
            <tr>

                <td>
                    <span class="score ${scoreClass}">
                        ${b.deal_score || 0}
                    </span>
                </td>

                <td>
                    <a href="${b.url}" target="_blank">
                        ${b.model}
                    </a>
                </td>

                <td>
                    ${b.price || "-"} €
                </td>

                <td>
                    ${b.old_price || "-"} €
                </td>

                <td class="discount">
                    -${b.discount || 0}%
                </td>

                <td>
                    ${b.weight || "-"}
                </td>

                <td>
                    ${b.groupset || "-"}
                </td>

                <td>
                    ${b.dealer || "-"}
                </td>

            </tr>
        `;
    });
}

function sortBy(field) {

    currentSort = field;

    loadBikes();
}

document
    .getElementById("carbonOnly")
    .addEventListener(
        "change",
        loadBikes
    );

loadBikes();