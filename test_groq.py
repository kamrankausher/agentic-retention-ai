import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
key = os.environ.get("GROQ_API_KEY")

print("Key starts with:", key[:10] if key else "None")

try:
    client = OpenAI(
        api_key=key,
        base_url="https://api.groq.com/openai/v1"
    )
    
    response = client.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[{"role": "user", "content": "Say hello"}],
    )
    print("SUCCESS! API responded:", response.choices[0].message.content)
except Exception as e:
    print("ERROR:", e)
