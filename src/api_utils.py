import requests
import pandas as pd
import time
from datetime import datetime
from bs4 import BeautifulSoup


def make_api_request(url, params=None, timeout=5):
    """Make an API request with error handling"""
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout:
        print("⏳ Request timed out")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Other Error: {e}")
        return None


def get_joke():
    """Get a random joke from the Official Joke API"""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = make_api_request(url)
    if response and response.status_code == 200:
        data = response.json()
        return data["setup"], data["punchline"]
    return None, None


def get_dog_images(count=1):
    """Get random dog images from Dog CEO API"""
    url = f"https://dog.ceo/api/breeds/image/random/{count}"
    response = make_api_request(url)
    if response and response.status_code == 200:
        data = response.json()
        return data["message"]
    return []


def get_weather(city, api_key):
    """Get weather data from OpenWeatherMap API"""
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = make_api_request(url, params=params)
    if response and response.status_code == 200:
        return response.json()
    return None


def get_cat_facts(limit=10, page=1):
    """Get cat facts from Cat Facts API"""
    url = "https://catfact.ninja/facts"
    params = {"limit": limit, "page": page}

    response = make_api_request(url, params=params)
    if response and response.status_code == 200:
        return response.json()
    return None


def get_crypto_prices(coins=["bitcoin", "ethereum"], currency="usd"):
    """Get cryptocurrency prices from CoinGecko API"""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": ",".join(coins), "vs_currencies": currency}

    response = make_api_request(url, params=params)
    if response and response.status_code == 200:
        return response.json()
    return None


def collect_cat_facts_dataset(target_count=50):
    """Build a dataset of cat facts"""
    facts_list = []
    page = 1

    while len(facts_list) < target_count:
        data = get_cat_facts(limit=10, page=page)
        if data and "data" in data:
            facts = [fact["fact"] for fact in data["data"]]
            facts_list.extend(facts)
            print(f"📄 Page {page}: Collected {len(facts_list)} facts so far.")
            page += 1
            time.sleep(1)  # Respect rate limits
        else:
            print(f"Error on page {page}")
            break

    return facts_list


def track_crypto_prices(coins=["bitcoin", "ethereum"], interval=5, iterations=5):
    """Track cryptocurrency prices at regular intervals"""
    records = []

    try:
        for i in range(iterations):
            data = get_crypto_prices(coins)
            if data:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                record = {"timestamp": timestamp}

                for coin in coins:
                    if coin in data:
                        record[f"{coin}_usd"] = data[coin]["usd"]

                records.append(record)
                print(
                    f"{timestamp} | {', '.join([f'{coin.upper()}: ${record[f"{coin}_usd"]}' for coin in coins])}"
                )

            if i < iterations - 1:
                time.sleep(interval)

    except KeyboardInterrupt:
        print("\nStopped by user")

    return records


def nasa_image_search(query="moon", media_type="image", limit=3):
    """Search NASA images and scrape additional details"""
    api_url = "https://images-api.nasa.gov/search"
    params = {"q": query, "media_type": media_type}

    response = make_api_request(api_url, params=params)
    if not response or response.status_code != 200:
        return []

    data = response.json()
    items = data["collection"]["items"]
    records = []

    for item in items[:limit]:
        title = item["data"][0]["title"]
        nasa_url = item["links"][0]["href"]

        # Scrape the NASA image page for more details
        try:
            page_response = requests.get(nasa_url, timeout=5)
            soup = BeautifulSoup(page_response.text, "html.parser")

            # Try to extract description
            description = "No description found"
            meta_desc = soup.find("meta", attrs={"name": "description"})
            if meta_desc:
                description = meta_desc.get("content", "No description found")

            records.append(
                {
                    "title": title,
                    "url": nasa_url,
                    "description": description[:200] + "..."
                    if len(description) > 200
                    else description,
                }
            )

            print(f"✅ Collected: {title}")

        except Exception as e:
            print(f"❌ Failed to scrape {nasa_url}: {e}")

        time.sleep(1)  # Be polite to the server

    return records
