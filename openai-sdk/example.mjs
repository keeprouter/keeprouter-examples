// Call a chat-compatible model through KeepRouter with the OpenAI SDK.
//
//   npm i openai
//   KEEPROUTER_KEY=sk-kr-your-key node example.mjs
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://keeprouter.com/v1",
  apiKey: process.env.KEEPROUTER_KEY,
});

// Start with a key scoped to free. For paid models, check the live catalog,
// enabled chat route, key scope, and balance before changing this exact ID.
const resp = await client.chat.completions.create({
  model: "free",
  messages: [{ role: "user", content: "In one sentence, what is an LLM API gateway?" }],
});
console.log(resp.choices[0].message.content);
