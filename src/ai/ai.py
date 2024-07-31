import ollama

async def chat( message):
    message = [
        {
            "content": message,
            "role": "user",
            # "timestamp": datetime.now().isoformat(),
        }
    ]

    print(f"Sending message to Ollama")
    try:
        response = ollama.chat(model="phi3", messages=message)
        print(response["message"]["content"])
        return response["message"]["content"]
    except Exception as e:
        print(f"Error: {e}")