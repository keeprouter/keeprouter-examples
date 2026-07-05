// Call any model through KeepRouter with the OpenAI SDK.
//
//   npm i openai
//   KEEPROUTER_KEY=sk-kr-your-key node example.mjs
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://keeprouter.com/v1",
  apiKey: process.env.KEEPROUTER_KEY,
});

// Swap the model id for any model in the catalog (https://keeprouter.com/models):
// claude-opus-4-8, gpt-4o, gemini-3.5-flash, deepseek-v3.2, glm-4.6, free, …
const resp = await client.chat.completions.create({
  model: "gemini-3.5-flash",
  messages: [{ role: "user", content: "In one sentence, what is an LLM API gateway?" }],
});
console.log(resp.choices[0].message.content);
