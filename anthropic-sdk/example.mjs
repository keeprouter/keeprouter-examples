// Call Claude (and more) through KeepRouter with the Anthropic SDK.
//
//   npm i @anthropic-ai/sdk
//   KEEPROUTER_KEY=sk-kr-your-key node example.mjs
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: "https://keeprouter.com",
  apiKey: process.env.KEEPROUTER_KEY,
});

const resp = await client.messages.create({
  model: "claude-opus-4-8",
  max_tokens: 1024,
  messages: [{ role: "user", content: "In one sentence, what is an LLM API gateway?" }],
});
console.log(resp.content[0].text);
