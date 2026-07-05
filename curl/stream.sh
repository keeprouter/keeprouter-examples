#!/usr/bin/env bash
# Streaming chat completion (server-sent events). Set KEEPROUTER_KEY first.
#   export KEEPROUTER_KEY=sk-kr-your-key
set -euo pipefail

curl -N https://keeprouter.com/v1/chat/completions \
  -H "Authorization: Bearer $KEEPROUTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "glm-4.6",
    "stream": true,
    "messages": [{"role": "user", "content": "Count to five."}]
  }'
