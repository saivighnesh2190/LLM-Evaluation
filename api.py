
import config
from typing import Any
import network
import time

    
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
    start=time.perf_counter()
    data = network.make_post_request(
        config.BASE_URL,
        headers,
        payload
    )
    latency=time.perf_counter()-start
    if data is None:
        return None
    try:
        return {
            "responses": data["choices"][0]["message"]["content"],
            "model": data["model"],
            "prompt_tokens": data["usage"]["prompt_tokens"],
            "completion_tokens": data["usage"]["completion_tokens"],
            "total_tokens": data["usage"]["total_tokens"],
            "latency":round(latency,3)
        }
    except (KeyError,IndexError,TypeError):
        return None

    

