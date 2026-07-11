import api
import utils
PROMPTS_FILE="prompts.json"
    
def main():
    results=[]
    prompts=utils.load_json(PROMPTS_FILE)
    for prompt in prompts:
        model_details=api.ask_llm(prompt["prompt"])
        if model_details is None:
            continue
        result = {
            "id": prompt["id"],
            "prompt": prompt["prompt"],
            "response":model_details["response"],
            "model_name":model_details["model"],
            "latency":model_details["latency"]

        }
        results.append(result)
    utils.save_json(results, "results.json")





if __name__=="__main__":
    main()
