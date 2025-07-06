# FIP-Lite
The idea of enabling tool use in LLMs without structured APIs. Think of this as a prototype for agent-OS-style workflows.

# FIP-Lite 🔧🧠

FIP-Lite (Function Invocation Protocol Lite) is a lightweight framework that enables **LLMs to safely call Python functions** using natural language. It uses YAML-style structured prompts and a custom execution engine to bridge LLM outputs with local Python logic — no fine-tuning or native tool-calling required.

## 🌟 Key Features

- 🔍 Parses LLM output from DeepSeek/GPT using custom YAML tags (`<FUNCTION_CALL>`)
- 📦 Routes parsed instructions to registered Python functions
- 📊 Includes sample functions like `generate_report()` and `say_hello()`
- 🧪 Simple `main.py` loop for interactive testing

---

## 📁 Project Structure
fip-lite/
├── fip_lite.py # Extracts and routes function calls from LLM output
├── fip_runtime.py # Registry and executor for Python functions
├── LLMs_Call.py # Connects to OpenRouter / DeepSeek to get LLM completions
├── main.py # CLI interface for testing
├── requirements.txt # Dependencies
├── .env.example # Sample env file (e.g., API keys)
├── .gitignore # Ignore sensitive and unnecessary files
└── README.md # You're here!

---

## 🚀 How to Run

1. **Install dependencies**
  
```bash
pip install -r requirements.txt
```
2. **Set your environment variable**

Create/Edit .env to include your OPENROUTER_API_KEY.

3. **Run the app**

```bash
python main.py
```
Enter natural language requests, like: [How can I assist you today? → I want a report for the Middle East from Jan to June 2024.]

3. **Example Function Output**
```bash
How can I assist you today?(or type 'exit' to quit): My name is Salem
LLM Output:
 <FUNCTION_CALL>
invoke: say_hello
input:
  name: Salem
</FUNCTION_CALL>

I'm inside the [say_hello] function 

Function Result:
 {"status": "success", "output": {"message": "Hello, Salem! Welcome to the system."}}
```
4. **Add Your Own Functions**
```bash
@fip_function("my_function")
def my_function(arg1: str) -> dict:
    return {"result": f"You said {arg1}"}

```
5. **LLMs Tested**
-deepseek/deepseek-r1:free via OpenRouter.ai
6. **License**
-This project is licensed under the MIT License – see the LICENSE file for details.
   
