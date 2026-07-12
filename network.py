from typing import Any
import logger_config
import requests
import config
import time
import logging
logger = logging.getLogger(__name__)

def make_get_request(url: str) -> Any | None:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("NETWORK ERROR:", e)
        return None


def make_post_request(
    url: str,
    headers: dict[str, str],
    payload: dict[str, Any],
) -> Any | None:
    for attempt in range(3):
        response = None
        try:
            logger.info(f"sending the request -> -> ->")
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=config.TIMEOUT,
            )
            response.raise_for_status()
            logger.info("getting the request <- <- <-")
            return response.json()
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                wait_time=2** attempt
                logger.warning(f"Attempt {attempt+1}/3:"
                    f"429 received .Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                continue
            logger.error("Maximum retries exceeded.")
            return None
        except requests.exceptions.RequestException as e:
            logger.error("NETWORK ERROR:", e)
            return None
