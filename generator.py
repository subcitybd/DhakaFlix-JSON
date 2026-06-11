import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

SOURCE = "http://172.16.50.9"

def get_listing():
    try:
        r = requests.get(SOURCE, timeout=10)
        return r.text
    except:
        return ""

html = get_listing()
soup = BeautifulSoup(html, "html.parser")

movies = []
tv = []
korean = []

# extract all links from folder listing
for a in soup.find_all("a"):
    href = a.get("href")

    if not href:
        continue

    full_url = urljoin(SOURCE, href)
    name = href.strip("/")

    # ignore parent folder links
    if name in ["../", "/"]:
        continue

    lower = name.lower()

    # classify intelligently
    if any(x in lower for x in ["movie", "film", ".mp4", ".mkv", ".m3u8"]):
        movies.append({"name": name, "url": full_url})

    elif any(x in lower for x in ["s01", "episode", "tv", "series"]):
        tv.append({"name": name, "url": full_url})

    elif "korean" in lower or "kr" in lower:
        korean.append({"name": name, "url": full_url})

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

with open("movies.json", "w") as f:
    json.dump(movies, f, indent=2)

with open("tv.json", "w") as f:
    json.dump(tv, f, indent=2)

with open("korean.json", "w") as f:
    json.dump(korean, f, indent=2)

with open("repo.json", "w") as f:
    json.dump(repo, f, indent=2)

print("DhakaFlix updated successfully")
