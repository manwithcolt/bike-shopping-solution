import json

def load():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return []

def save(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

bikes = load()

# Demo-Daten (später echte Shops)
new_bike = {
    "dealer": "Canyon",
    "model": "Grizl CF SL",
    "price": 2399,
    "frame": "carbon",
    "url": "https://www.canyon.com"
}

if not any(
    b.get("model") == new_bike["model"]
    and b.get("dealer") == new_bike["dealer"]
    for b in bikes
):
    bikes.append(new_bike)
