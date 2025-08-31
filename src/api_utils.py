import requests
import pandas as pd
import time
from datetime import datetime
from bs4 import BeautifulSoup
import logging
from typing import List, Dict, Optional, Tuple, Any

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def make_api_request(
    url: str, params: Optional[Dict] = None, timeout: int = 5
) -> Optional[requests.Response]:
    """Make an API request with comprehensive error handling"""
    try:
        response = requests.get(url, params=params, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout:
        logger.warning("Request timed out for URL: %s", url)
        return None
    except requests.exceptions.HTTPError as e:
        logger.error("HTTP Error for URL %s: %s", url, e)
        return None
    except requests.exceptions.RequestException as e:
        logger.error("Request failed for URL %s: %s", url, e)
        return None


def get_joke() -> Tuple[Optional[str], Optional[str]]:
    """Get a random joke from the Official Joke API"""
    url = "https://official-joke-api.appspot.com/random_joke"
    response = make_api_request(url)

    if response and response.status_code == 200:
        try:
            data = response.json()
            return data.get("setup"), data.get("punchline")
        except (ValueError, KeyError) as e:
            logger.error("Failed to parse joke response: %s", e)

    return None, None


def get_dog_images(count: int = 1) -> List[str]:
    """Get random dog images from Dog CEO API"""
    if count < 1:
        return []

    url = f"https://dog.ceo/api/breeds/image/random/{count}"
    response = make_api_request(url)

    if response and response.status_code == 200:
        try:
            data = response.json()
            return data.get("message", [])
        except (ValueError, KeyError) as e:
            logger.error("Failed to parse dog images response: %s", e)

    return []


def get_weather(city: str, api_key: str) -> Optional[Dict]:
    """Get weather data from OpenWeatherMap API"""
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = make_api_request(url, params=params)

    if response and response.status_code == 200:
        try:
            return response.json()
        except ValueError as e:
            logger.error("Failed to parse weather response: %s", e)

    return None


def get_cat_facts(limit: int = 10, page: int = 1) -> Optional[Dict]:
    """Get cat facts from Cat Facts API"""
    url = "https://catfact.ninja/facts"
    params = {"limit": limit, "page": page}

    response = make_api_request(url, params=params)

    if response and response.status_code == 200:
        try:
            return response.json()
        except ValueError as e:
            logger.error("Failed to parse cat facts response: %s", e)

    return None


def get_crypto_prices(coins: List[str] = None, currency: str = "usd") -> Optional[Dict]:
    """Get cryptocurrency prices from CoinGecko API"""
    if coins is None:
        coins = ["bitcoin", "ethereum"]

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": ",".join(coins), "vs_currencies": currency}

    response = make_api_request(url, params=params)

    if response and response.status_code == 200:
        try:
            return response.json()
        except ValueError as e:
            logger.error("Failed to parse crypto prices response: %s", e)

    return None


def collect_cat_facts_dataset(target_count: int = 50) -> List[str]:
    """Build a dataset of cat facts"""
    facts_list = []
    page = 1

    while len(facts_list) < target_count:
        data = get_cat_facts(limit=min(10, target_count - len(facts_list)), page=page)

        if data and "data" in data:
            facts = [fact["fact"] for fact in data["data"] if "fact" in fact]
            facts_list.extend(facts)
            logger.info("Page %d: Collected %d facts so far.", page, len(facts_list))

            if len(facts) == 0:  # No more facts available
                break

            page += 1
            time.sleep(1)  # Respect rate limits
        else:
            logger.error("Error on page %d", page)
            break

    return facts_list[:target_count]  # Ensure we don't exceed target


def track_crypto_prices(
    coins: List[str] = None, interval: int = 5, iterations: int = 5
) -> List[Dict]:
    """Track cryptocurrency prices at regular intervals"""
    if coins is None:
        coins = ["bitcoin", "ethereum"]

    records = []

    try:
        for i in range(iterations):
            data = get_crypto_prices(coins)
            if data:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                record = {"timestamp": timestamp}

                for coin in coins:
                    coin_key = f"{coin}_usd"
                    if coin in data and "usd" in data[coin]:
                        record[coin_key] = data[coin]["usd"]
                    else:
                        record[coin_key] = None

                records.append(record)

                # Format the price string safely
                price_strings = []
                for coin in coins:
                    price = record.get(f"{coin}_usd")
                    price_str = f"{price:.2f}" if price is not None else "N/A"
                    price_strings.append(f"{coin.upper()}: ${price_str}")

                logger.info("%s | %s", timestamp, ", ".join(price_strings))

            if i < iterations - 1:
                time.sleep(interval)

    except KeyboardInterrupt:
        logger.info("Stopped by user")

    return records


def nasa_image_search(
    query: str = "moon", media_type: str = "image", limit: int = 3
) -> List[Dict]:
    """Search NASA images and scrape additional details"""
    api_url = "https://images-api.nasa.gov/search"
    params = {"q": query, "media_type": media_type}

    response = make_api_request(api_url, params=params)
    if not response or response.status_code != 200:
        return []

    try:
        data = response.json()
        items = data.get("collection", {}).get("items", [])
    except ValueError as e:
        logger.error("Failed to parse NASA API response: %s", e)
        return []

    records = []

    for item in items[:limit]:
        try:
            title = item["data"][0].get("title", "Untitled")
            links = item.get("links", [])
            nasa_url = links[0].get("href") if links else None

            if not nasa_url:
                continue

            # Scrape the NASA image page for more details
            try:
                page_response = requests.get(nasa_url, timeout=5)
                soup = BeautifulSoup(page_response.text, "html.parser")

                # Try to extract description
                description = "No description found"
                meta_desc = soup.find("meta", attrs={"name": "description"})
                if meta_desc:
                    description = meta_desc.get("content", "No description found")

                # Truncate description if too long
                if len(description) > 200:
                    description = description[:197] + "..."

                records.append(
                    {
                        "title": title,
                        "url": nasa_url,
                        "description": description,
                    }
                )

                logger.info("Collected: %s", title)

            except Exception as e:
                logger.error("Failed to scrape %s: %s", nasa_url, e)

            time.sleep(1)  # Be polite to the server

        except (KeyError, IndexError) as e:
            logger.error("Failed to process NASA item: %s", e)
            continue

    return records
