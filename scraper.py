import json
from datetime import date

TODAY = str(date.today())

new_bikes = [
    {
        "dealer": "Canyon",
        "source": "Canyon Sale",
        "model": "Grail CF 8 1by",
        "image": "https://images.unsplash.com/photo-1541625602330-2277a4c46182",
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
        "source": "Canyon Sale",
        "model": "Grail CF 7",
        "image": "https://images.unsplash.com/photo-1511994298241-608e28f14fde",
        "category": "Gravel",
        "frame": "Carbon",
        "groupset": "Shimano GRX 820",
        "weight": "9.10 kg",
        "price": 1999,
        "old_price": 2499,
        "discount": 20,
        "deal_score": 90,
        "url": "https://www.canyon.com"
    },
    {
        "dealer": "Canyon",
        "source": "Canyon Sale",
        "model": "Grizl CF SL 8",
        "image": "https://images.unsplash.com/photo-1507035895480-2b3156c31fc8",
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
        "source": "Canyon Sale",
        "model": "Grizl CF SL 7",
        "image": "https://images.unsplash.com/photo-1558981806-ec527fa84c39",
        "category": "Gravel",
        "frame": "Carbon",
        "groupset": "Shimano GRX 610",
        "weight": "9.30 kg",
        "price": 2199,
        "old_price": 2699,
        "discount": 19,
        "deal_score": 87,
        "url": "https://www.canyon.com"
    },
    {
        "dealer": "Canyon",
        "source": "Canyon Sale",
        "model": "Endurace CF 7",
        "image": "https://images.unsplash.com/photo-1485965120184-e220f721d03e",
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