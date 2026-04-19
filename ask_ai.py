import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Загружаем переменные из .env
load_dotenv(Path(__file__).parent / ".env")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key or api_key.startswith("["):
    print("❌ Ошибка: замените плейсхолдер в .env на настоящий ключ sk-...")
    exit(1)

client = OpenAI(api_key=api_key)

PROJECT_DESCRIPTION = "приложение для ведения заметок по итогам личных встреч"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": (
                f"Придумай 3 креативных названия для моего проекта: {PROJECT_DESCRIPTION}"
            ),
        }
    ],
)

print(response.choices[0].message.content)
