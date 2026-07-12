from typing import Any
import requests
import config
import time


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
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=config.TIMEOUT,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if response is not None and response.status_code == 429 and attempt < 2:
                time.sleep(2 ** attempt)
                continue
            print("NETWORK ERROR:", e)
            return None
        except requests.exceptions.RequestException as e:
            print("NETWORK ERROR:", e)
            return None
