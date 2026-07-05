"""Call Claude (and more) through KeepRouter with the Anthropic SDK.

    pip install anthropic
    export KEEPROUTER_KEY=sk-kr-your-key
    python example.py
"""
import os

from anthropic import Anthropic

client = Anthropic(
    base_url="https://keeprouter.com",
    api_key=os.environ["KEEPROUTER_KEY"],
)

resp = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "In one sentence, what is an LLM API gateway?"}],
)
print(resp.content[0].text)
