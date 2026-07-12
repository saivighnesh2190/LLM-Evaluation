
import config
from typing import Any
import network
import time
from logger_config import logger
import logging
logger = logging.getLogger(__name__)
def ask_llm(prompt: str)->dict[str,Any] | None:

    payload = {
        "model": config.MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {config.API_KEY}",
        "Content-Type": "application/json"
    }
    logger.info(f"Sending request to model :{config.MODEL_NAME}")
    start=time.perf_counter()
    data = network.make_post_request(
        config.BASE_URL,
        headers,
        payload
    )
    latency=time.perf_counter()-start
    logger.info(f"Response recieved Successfully")
    if data is None:
        return None
    try:
        return {
            "response": data["choices"][0]["message"]["content"],
            "model": data["model"],
            "prompt_tokens": data["usage"]["prompt_tokens"],
            "completion_tokens": data["usage"]["completion_tokens"],
            "total_tokens": data["usage"]["total_tokens"],
            "latency":round(latency,3)
        }
    except (KeyError,IndexError,TypeError) as e:
        logger.error(f"Failed to parse API response:{e}")
        return None

    

