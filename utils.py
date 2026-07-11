import json
from typing import Any
def load_json(file_path:str)->Any:
    try:
        with open(file_path,"r",encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' contains invalid JSON.")
        return []
   
def save_json(data, file_path:str)->bool:

    with open(file_path,"w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)
    return True
   