#!/usr/bin/env bash
# OpenAI-compatible chat completion. Set KEEPROUTER_KEY first.
#   export KEEPROUTER_KEY=sk-kr-your-key
set -euo pipefail

curl https://keeprouter.com/v1/chat/completions \
  -H "Authorization: Bearer $KEEPROUTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "free",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
