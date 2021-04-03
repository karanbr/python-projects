capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Munich"]
}

print(travel_log["Germany"][1])

# Nesting Dictionary in a Dictionary

travel_log_2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "cities_visited": ["Hamburg", "Berlin", "Munich"]
    }
}

# Nesting Dictionaries inside a List

travel_log_3 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Hamburg", "Berlin"],
        "total_visits": 24
    }
]

print(travel_log_3[1]["cities_visited"][1])
