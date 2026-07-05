"""Call any model through KeepRouter with the OpenAI SDK.

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

# Swap the model id for any model in the catalog (https://keeprouter.com/models):
# claude-opus-4-8, gpt-4o, gemini-3.5-flash, deepseek-v3.2, glm-4.6, free, …
resp = client.chat.completions.create(
    model="claude-opus-4-8",
    messages=[{"role": "user", "content": "In one sentence, what is an LLM API gateway?"}],
)
print(resp.choices[0].message.content)

# Streaming works the same way:
# for chunk in client.chat.completions.create(model="glm-4.6", messages=[...], stream=True):
#     print(chunk.choices[0].delta.content or "", end="")
