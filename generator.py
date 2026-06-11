import json
import requests

SOURCE = "http://172.16.50.9"

def fetch_source():
    try:
        r = requests.get(SOURCE, timeout=10)
        return r.text.lower()
    except:
        return ""

raw = fetch_source()

movies = []
tv = []
korean = []

if "movie" in raw:
    movies.append({
        "name": "Auto Movie",
        "url": SOURCE + "/movie.m3u8"
    })

if "tv" in raw:
    tv.append({
        "name": "Auto TV",
        "url": SOURCE + "/tv.m3u8"
    })

if "korean" in raw:
    korean.append({
        "name": "Auto Korean",
        "url": SOURCE + "/korean.m3u8"
    })

with open("movies.json", "w") as f:
    json.dump(movies, f, indent=2)

with open("tv.json", "w") as f:
    json.dump(tv, f, indent=2)

with open("korean.json", "w") as f:
    json.dump(korean, f, indent=2)

repo = {
    "name": "DhakaFlix",
    "author": "subcitybd",
    "version": 1,
    "catalogs": [
        {"name": "Movies", "url": "movies.json"},
        {"name": "TV Shows", "url": "tv.json"},
        {"name": "Korean TV", "url": "korean.json"}
    ]
}

with open("repo.json", "w") as f:
    json.dump(repo, f, indent=2)

print("done")
