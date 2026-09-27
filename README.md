# KeepRouter API examples

Small, inspectable examples for the OpenAI SDK, Anthropic SDK, Claude Code, and curl. KeepRouter model IDs and enabled routes can change; choose an exact ID from the [live model catalog][models] before using a paid model.

| Your task | Start here |
| --- | --- |
| Make a first chat request with the published **free** model | [Quickstart][quickstart] and the [Python](openai-sdk/example.py) or [Node](openai-sdk/example.mjs) OpenAI SDK example |
| Move an OpenAI or OpenRouter client | [Credential-free migration checker][checker], then [review the migration starter source][starter] |
| Configure Claude Code with a Claude model | [Claude Code guide][claude-guide] and [base URL settings](claude-code/settings.json) |
| Diagnose a failed request | [Error reference][errors] |
| Estimate a paid model's usage cost | [Live model catalog][models] and [cost calculator][cost] |

The migration checker runs in your browser. Paste only configuration with credentials and private request content removed. It does not translate OpenRouter model slugs or provider-specific fields automatically; select a current KeepRouter model ID and test the actual route. The separate [migration starter repository][starter] has dry-run Python and Node examples for a larger migration.

## First chat request: OpenAI SDK

Create a key scoped to **free** using the [quickstart][quickstart]. Set KEEPROUTER_KEY in your own shell or secret manager; never put a real key in source control. Install the SDK with pip install openai or npm install openai.

~~~python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://keeprouter.com/v1",
    api_key=os.environ["KEEPROUTER_KEY"],
)
response = client.chat.completions.create(
    model="free",
    messages=[{"role": "user", "content": "Hello"}],
)
print(response.choices[0].message.content)
~~~

Run the [Python](openai-sdk/example.py), [Node](openai-sdk/example.mjs), or [curl](curl/chat.sh) version. These examples use Chat Completions; a model being listed in the catalog does not mean it supports every API route. For a paid model, create a key with that model in its scope and check its published price and endpoint first. The [OpenAI SDK setup guide][openai-guide] explains the /v1 base URL and common 401/404 mistakes.

## Anthropic SDK and Claude Code

The [Anthropic SDK examples](anthropic-sdk/) use the Messages API with a Claude model. They require a key scoped to the selected model and sufficient paid balance. https://keeprouter.com is the SDK/Claude Code base URL; do not append /v1 to it. The [Messages curl example](curl/messages.sh) uses the full /v1/messages operation URL.

For Claude Code, keep the base URL in [claude-code/settings.json](claude-code/settings.json) and inject the token through your shell or secret manager:

~~~bash
export ANTHROPIC_BASE_URL=https://keeprouter.com
export ANTHROPIC_AUTH_TOKEN="$KEEPROUTER_KEY"
claude
~~~

Use a Claude model selected from the live catalog. [Anthropic's gateway documentation](https://code.claude.com/docs/en/llm-gateway) says routing Claude Code to non-Claude models through a gateway is unsupported. A translated Messages request working once does not prove full Claude Code compatibility, including tools, streaming, or future versions. See the [KeepRouter Claude Code guide][claude-guide] for setup and verification.

## Request an example or report a reproducible problem

[Open an example request](https://github.com/keeprouter/keeprouter-examples/issues/new?template=example-request.yml) with the client, endpoint, exact model ID, and a minimal sanitized reproduction. Never post API keys, private prompts, or customer data in a public issue. The [Issues list](https://github.com/keeprouter/keeprouter-examples/issues) tracks real requests and fixes.

These examples are starting points, not a claim that every model, client version, or feature combination has been tested. No paid inference request is needed to review this repository.

## License

[MIT](LICENSE)

[quickstart]: https://keeprouter.com/docs/quickstart?utm_source=github&utm_medium=referral&utm_campaign=sdk-migration
[checker]: https://keeprouter.com/tools/api-migration-checker?utm_source=github&utm_medium=referral&utm_campaign=sdk-migration
[starter]: https://github.com/Digidai/keeprouter-migration-starter
[models]: https://keeprouter.com/models?utm_source=github&utm_medium=referral&utm_campaign=sdk-migration
[claude-guide]: https://keeprouter.com/use-cases/claude-code?utm_source=github&utm_medium=referral&utm_campaign=sdk-migration
[openai-guide]: https://keeprouter.com/use-cases/openai-sdk?utm_source=github&utm_medium=referral&utm_campaign=sdk-migration
[errors]: https://keeprouter.com/docs/errors?utm_source=github&utm_medium=referral&utm_campaign=sdk-migration
[cost]: https://keeprouter.com/tools/api-cost-calculator?utm_source=github&utm_medium=referral&utm_campaign=sdk-migration
