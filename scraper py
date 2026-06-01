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
bikes.append({
    "dealer": "Canyon",
    "model": "Grizl CF SL",
    "price": 2399,
    "frame": "carbon",
    "url": "https://www.canyon.com"
})

save(bikes)