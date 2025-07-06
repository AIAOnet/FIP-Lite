import fip_lite
import LLMs_Call


if __name__ == "__main__":
    while True:
        
        user_input = input("How can I assist you today?(or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        
        
        respons= LLMs_Call.get_respons(user_input)
        
        
        
        
        
        
        print("LLM Output:\n", respons)
        result = fip_lite.extract_function_call(respons)
        print("Function Result:\n", result)