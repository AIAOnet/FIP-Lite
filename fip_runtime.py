
import json
from typing import Callable, Dict, Any

FUNCTIONS: Dict[str, Callable[..., Any]] = {}

# Decorator to register a function
def fip_function(name: str):
    def decorator(func: Callable):
        FUNCTIONS[name] = func
        return func
    return decorator

# Example function
@fip_function("generate_report")
def generate_report(start_date: str, end_date: str, region: str = "NA") -> Dict[str, Any]:
    print("\n\nI'm inside the [generate_report] function \n\n")
    return {
        "report_url": f"https://reports.example.com/{region}/{start_date}_{end_date}.pdf",
        "summary": f"Report for {region} from {start_date} to {end_date}."
    }

@fip_function("say_hello")
def say_hello(name: str) -> Dict[str, Any]:
    print("\n\nI'm inside the [say_hello] function \n\n")
    return {
        "message": f"Hello, {name}! Welcome to the system."
    }

# Execution engine
def execute(invocation_json: str) -> str:
    try:
        data = json.loads(invocation_json)
        func_name = data.get("invoke")
        args = data.get("input", {})

        if func_name not in FUNCTIONS:
            return json.dumps({
                "status": "error",
                "error": {
                    "code": "NotFound",
                    "message": f"Function '{func_name}' is not registered."
                }
            })

        result = FUNCTIONS[func_name](**args)
        return json.dumps({
            "status": "success",
            "output": result
        })

    except Exception as e:
        return json.dumps({
            "status": "error",
            "error": {
                "code": "RuntimeError",
                "message": str(e)
            }
        })
