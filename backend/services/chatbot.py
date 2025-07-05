import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def chat_with_ai(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
