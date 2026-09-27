#!/usr/bin/env bash
# Anthropic-compatible Messages API (the endpoint Claude Code + the Anthropic SDK use).
# Paid example: scope the key to this model and check balance and price first.
#   export KEEPROUTER_KEY=sk-kr-your-key
set -euo pipefail

curl https://keeprouter.com/v1/messages \
  -H "x-api-key: $KEEPROUTER_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-opus-4-8",
    "max_tokens": 1024,
    "messages": [{"role": "user", "content": "Hello"}]
  }'
