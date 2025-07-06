from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

LLM_api_key = os.getenv('OPENROUTER_API_KEY')


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=LLM_api_key,
)

PROMPT_TEMPLATE = """You are a system interface to call specific functions.
Your job is to choose the correct function and return the input values in this format:

<FUNCTION_CALL>
invoke: function_name
input:
  param1: value1
  param2: value2
</FUNCTION_CALL>

Functions available:
- generate_report(start_date: string, end_date: string, region: [NA, EU, ME, APAC])
- say_hello(name: string)

Only return the FUNCTION_CALL block. Do not explain.
"""





def get_respons(msg):
    
    
    completion = client.chat.completions.create(
   
    extra_body={},
    model="deepseek/deepseek-r1:free",
    #deepseek/deepseek-r1:free
    #deepseek/deepseek-r1-distill-llama-70b:free
    messages=[
           {
      "role": "system",
      "content": f"{PROMPT_TEMPLATE}"
    },
        
        {
        "role": "user",
        "content": f'{msg}'}
    ]
    )
    
    LLM_resp=completion.choices[0].message.content
    response =LLM_resp
   
    #print(response)
   
    return response


if __name__ == "__main__":
    get_respons('hello, my name is Salem')