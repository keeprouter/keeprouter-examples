# KeepRouter examples

One API key for **Claude, GPT, Gemini and 50+ models** — through the **OpenAI *and* Anthropic** APIs. Runnable examples for calling [KeepRouter](https://keeprouter.com) from **Claude Code**, the **OpenAI SDK**, the **Anthropic SDK**, and **curl**.

> Get a key at **[keeprouter.com](https://keeprouter.com)** — new accounts get free trial credit, and the `free` model is **$0**. Billed at cost (0% token markup), pay-as-you-go, no monthly fee.

## Run Claude Code on cheaper models (2 lines)

Claude Code speaks Anthropic's Messages API, and KeepRouter serves it natively. Point Claude Code at KeepRouter:

```bash
export ANTHROPIC_BASE_URL=https://keeprouter.com
export ANTHROPIC_AUTH_TOKEN=sk-kr-your-key
claude
```

Then switch models inside Claude Code with `/model <id>` — keep `claude-opus-4-8` for the hard turns, drop to `glm-4.6`, `deepseek-v3.2`, or `kimi-k2.6` for routine ones (often **10–30× cheaper**). Streaming, tool use, and extended thinking pass straight through — no translator or proxy.

Prefer a file? See [`claude-code/settings.json`](claude-code/settings.json) for `~/.claude/settings.json`.
Full guide with a per-turn cost table: **<https://keeprouter.com/use-cases/claude-code>**

## OpenAI SDK — one `base_url` change

Your existing OpenAI code, pointed at KeepRouter, now reaches every model — just change the model id:

```python
from openai import OpenAI

client = OpenAI(base_url="https://keeprouter.com/v1", api_key="sk-kr-your-key")
r = client.chat.completions.create(
    model="claude-opus-4-8",   # or gpt-4o, gemini-3.5-flash, deepseek-v3.2, free, …
    messages=[{"role": "user", "content": "Hello"}],
)
print(r.choices[0].message.content)
```

Runnable: [`openai-sdk/example.py`](openai-sdk/example.py) · [`openai-sdk/example.mjs`](openai-sdk/example.mjs) · guide: <https://keeprouter.com/use-cases/openai-sdk>

## Anthropic SDK

The Anthropic SDK works the same way — same key, native Messages API:

```python
from anthropic import Anthropic

client = Anthropic(base_url="https://keeprouter.com", api_key="sk-kr-your-key")
r = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
)
print(r.content[0].text)
```

Runnable: [`anthropic-sdk/example.py`](anthropic-sdk/example.py) · [`anthropic-sdk/example.mjs`](anthropic-sdk/example.mjs)

## curl

```bash
curl https://keeprouter.com/v1/chat/completions \
  -H "Authorization: Bearer $KEEPROUTER_KEY" -H "Content-Type: application/json" \
  -d '{"model":"claude-opus-4-8","messages":[{"role":"user","content":"Hello"}]}'
```

More: [`curl/`](curl/) — chat, Anthropic messages, and streaming.

## Models & pricing

Every model and its live per-token price: **<https://keeprouter.com/models>**. Machine-readable catalog for agents: [`/models.md`](https://keeprouter.com/models.md) and [`/llms.txt`](https://keeprouter.com/llms.txt).

## License

[MIT](LICENSE)
