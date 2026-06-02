import json

bikes = [
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
        "is_new": True,
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
        "is_new": True,
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
        "is_new": False,
        "url": "https://www.canyon.com"
    }
]

with open("data.json", "w") as f:
    json.dump(bikes, f, indent=2)