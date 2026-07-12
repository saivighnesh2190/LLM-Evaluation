import api
import utils
import logging
PROMPTS_FILE = "prompts.json"
logger = logging.getLogger(__name__)


def main():
    logger.info("Application started")
    results: list = []
    prompts = utils.load_json(PROMPTS_FILE)
    logger.info(f"Loaded {len(prompts)} prompts")

    if not isinstance(prompts, list):
        logger.error(f"Error: '{PROMPTS_FILE}' must contain a JSON array.")
        return

    if not prompts:
        logger.error(f"Error: No prompts found in '{PROMPTS_FILE}'.")
        return

    for prompt in prompts:
        logger.info(f"Processing Prompt ID {prompt['id']}")
        model_details = api.ask_llm(prompt["prompt"])
        if model_details is None:
            logger.error(f"Skipping prompt {prompt.get('id')}: request failed.")
            continue

        result = {
            "id": prompt["id"],
            "prompt": prompt["prompt"],
            "response": model_details["response"],
            "model_name": model_details["model"],
            "latency": model_details["latency"],
            "prompt_tokens": model_details["prompt_tokens"],
            "completion_tokens": model_details["completion_tokens"],
            "total_tokens": model_details["total_tokens"],
        }
        results.append(result)

    if not results:
        logger.error("No results were generated.")
        return

    utils.save_json(results, "results.json")
    logger.info(f"Saved {len(results)} result(s) to results.json")


if __name__ == "__main__":
    main()
