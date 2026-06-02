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
        "image": "https://images.unsplash.com/photo-1541625602330-2277a4c46182",
        "url": "https://www.canyon.com/de-de/gravel-bikes/race/grail/cf/grail-cf-8-1by/4148.html"
    },
    {
        "dealer": "Canyon",
        "model": "Grail CF 7",
        "category": "Gravel",
        "frame": "Carbon",
        "groupset": "Shimano GRX 820",
        "weight": "9.10 kg",
        "price": 1999,
        "old_price": 2499,
        "discount": 20,
        "deal_score": 90,
        "image": "https://images.unsplash.com/photo-1511994298241-608e28f14fde",
        "url": "https://www.canyon.com"
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
        "image": "https://images.unsplash.com/photo-1507035895480-2b3156c31fc8",
        "url": "https://www.canyon.com"
    },
    {
        "dealer": "Canyon",
        "model": "Grizl CF SL 7",
        "category": "Gravel",
        "frame": "Carbon",
        "groupset": "Shimano GRX 610",
        "weight": "9.30 kg",
        "price": 2199,
        "old_price": 2699,
        "discount": 19,
        "deal_score": 87,
        "image": "https://images.unsplash.com/photo-1558981806-ec527fa84c39",
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
        "image": "https://images.unsplash.com/photo-1485965120184-e220f721d03e",
        "url": "https://www.canyon.com"
    },
    {
        "dealer": "Canyon",
        "model": "Endurace CF 8",
        "category": "Road",
        "frame": "Carbon",
        "groupset": "Ultegra Di2",
        "weight": "7.90 kg",
        "price": 3499,
        "old_price": 3999,
        "discount": 13,
        "deal_score": 89,
        "image": "https://images.unsplash.com/photo-1517649763962-0c623066013b",
        "url": "https://www.canyon.com"
    },
    {
        "dealer": "Canyon",
        "model": "Ultimate CF SL 7",
        "category": "Road",
        "frame": "Carbon",
        "groupset": "Shimano 105 Di2",
        "weight": "7.60 kg",
        "price": 2899,
        "old_price": 3399,
        "discount": 15,
        "deal_score": 91,
        "image": "https://images.unsplash.com/photo-1571068316344-75bc76f77890",
        "url": "https://www.canyon.com"
    },
    {
        "dealer": "Canyon",
        "model": "Ultimate CF SL 8",
        "category": "Road",
        "frame": "Carbon",
        "groupset": "Ultegra Di2",
        "weight": "7.20 kg",
        "price": 3999,
        "old_price": 4499,
        "discount": 11,
        "deal_score": 88,
        "image": "https://images.unsplash.com/photo-1505705694340-019e1e335916",
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