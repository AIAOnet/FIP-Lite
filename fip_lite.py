import re
import yaml
import json
from fip_runtime import execute
import datetime


def convert_dates_to_strings(obj):
    if isinstance(obj, dict):
        return {k: convert_dates_to_strings(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_dates_to_strings(i) for i in obj]
    elif isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    else:
        return obj
    
def extract_function_call(llm_output: str) -> str:
    match = re.search(r"<FUNCTION_CALL>(.*?)</FUNCTION_CALL>", llm_output, re.DOTALL)
    if not match:
        raise ValueError("No FUNCTION_CALL block found in LLM output")

    
    
    raw_block = match.group(1).strip()

    

    #print(raw_block)
    
    try:

        parsed = yaml.safe_load(raw_block)

    except yaml.YAMLError as e:
        print("YAML parsing error:", e)

    print(parsed)
    
    parsed = yaml.safe_load(raw_block)

    cleaned_input = convert_dates_to_strings(parsed["input"])

    function_call = {
        "invoke": parsed["invoke"],
        "input": cleaned_input
    }
    print(function_call)
    print(json.dumps(function_call))
    return execute(json.dumps(function_call))
    
'''
    try:
    except Exception as e:
        return json.dumps({
            "status": "error",
            "error": {
                #"code": "ParseError",
                #"message": str(e)
            }
    
        })
    '''

if __name__ == "__main__":
    llm_output = '''
<FUNCTION_CALL>
invoke: generate_report
input:
  start_date: 2024-01-01
  end_date: 2024-06-30
  region: ME
</FUNCTION_CALL>
'''
    print("LLM Output:\n", llm_output)
    result = extract_function_call(llm_output)
    print("Function Result:\n", result)
