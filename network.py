from typing import Any
import requests
import config
def make_get_request(url: str) -> Any | None:
    try:
        response=requests.get(url,timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        return None
    except requests.exceptions.Timeout:
        return None
    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.JSONDecodeError:
        return None
    
def make_post_request(
    url: str,
    headers: dict[str,str],
    payload: dict[str,Any]
) -> Any:
    try:
        response = requests.post(url,headers=headers,json=payload,timeout=config.TIMEOUT)
        response.raise_for_status()
        return response.json()
    except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.Timeout,requests.exceptions.JSONDecodeError):
        return None