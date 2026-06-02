import json
from datetime import date

TODAY = str(date.today())

new_bikes = [
    {
        "dealer": "Canyon",
        "model": "Grail CF 8 1by",
        "category": "Gravel",
        "frame": "Carbon",
        "groupset": "Shimano GRX RX822 12s",
        "weight": "8.88 kg",
        "price": 2299,
        "old_price": 2999,
        "discount": 23,
        "deal_score": 96,
        "url": "https://www.canyon.com/de-de/gravel-bikes/race/grail/cf/grail-cf-8-1by/4148.html"
    },
    {
        "dealer": "Canyon",
        "model": "Grizl CF SL 8",
        "category": "Gravel",
        "frame": "Carbon",
        "groupset": "Shimano GRX 820",
        "weight": "8.90 kg",
        "price": 2399,
        "old_price": 2999,
        "discount": 20,
        "deal_score": 92,
        "url": "https://www.canyon.com"
    },
    {
        "dealer": "Canyon",
        "model": "Endurace CF 7",
        "category": "Road",
        "frame": "Carbon",
        "groupset": "Shimano 105 Di2",
        "weight": "8.20 kg",
        "price": 2499,
        "old_price": 2799,
        "discount": 11,
        "deal_score": 84,
        "url": "https://www.canyon.com"
    }
]

try:
    with open("data.json", "r") as f:
        old_bikes = json.load(f)
except:
    old_bikes = []

for bike in new_bikes:

    bike["is_new"] = True
    bike["price_dropped"] = False
    bike["first_seen"] = TODAY

    for old in old_bikes:

        if (
            old.get("dealer") == bike["dealer"]
            and old.get("model") == bike["model"]
        ):

            bike["is_new"] = False
            bike["first_seen"] = old.get(
                "first_seen",
                TODAY
            )

            if old.get("price", 999999) > bike["price"]:
                bike["price_dropped"] = True

            break

with open("data.json", "w") as f:
    json.dump(new_bikes, f, indent=2)