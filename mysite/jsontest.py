import json

obj = [
    {
        "did": 1,
        "name": "Au Bon Pain",
        "loc": "Bryan Center",
        "openTime": "14:00:00",
        "closeTime": "6:59:59"
    },
    {
        "did": 2,
        "name": "Cafe Edens",
        "loc": "McClendon Tower",
        "openTime": "00:00:00",
        "closeTime": "23:59:59"
    }
]

print json.dumps(obj)

