"""Call a chat-compatible model through KeepRouter with the OpenAI SDK.

    pip install openai
    export KEEPROUTER_KEY=sk-kr-your-key
    python example.py
"""
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://keeprouter.com/v1",
    api_key=os.environ["KEEPROUTER_KEY"],
)

# Start with a key scoped to free. For paid models, check the live catalog,
# enabled chat route, key scope, and balance before changing this exact ID.
resp = client.chat.completions.create(
    model="free",
    messages=[{"role": "user", "content": "In one sentence, what is an LLM API gateway?"}],
)
print(resp.choices[0].message.content)

# Streaming works the same way:
# for chunk in client.chat.completions.create(model="free", messages=[...], stream=True):
#     print(chunk.choices[0].delta.content or "", end="")
