import os
from dotenv import load_dotenv
from pymongo import MongoClient
from groq import Groq

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

print("=" * 50)
print("Testing MongoDB Connection")
print("=" * 50)

try:
    client = MongoClient(MONGODB_URI)

    # Ping MongoDB
    client.admin.command("ping")

    print("✅ MongoDB Connected Successfully")

    databases = client.list_database_names()
    print("Databases:", databases)

except Exception as e:
    print("❌ MongoDB Connection Failed")
    print(e)

print("\n" + "=" * 50)
print("Testing Groq Connection")
print("=" * 50)

try:
    groq_client = Groq(api_key=GROQ_API_KEY)

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": "Say hello"
            }
        ],
        max_tokens=10
    )

    print("✅ Groq Connected Successfully")
    print("Response:")
    print(response.choices[0].message.content)

except Exception as e:
    print("❌ Groq Connection Failed")
    print(e)