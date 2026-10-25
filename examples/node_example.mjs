/**
 * 随性 API Node.js 调用示例
 * 接口: https://api.ns666.cfd/v1
 * 文档: https://blog.ns666.cfd
 */

import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.SUIXING_API_KEY ?? "your-key-here",
  baseURL: "https://api.ns666.cfd/v1",
});

const MODEL = "deepseek-v4-flash";

/** 普通调用 */
async function simpleChat(prompt) {
  const resp = await client.chat.completions.create({
    model: MODEL,
    messages: [{ role: "user", content: prompt }],
  });
  return resp.choices[0].message.content;
}

/** 流式调用 */
async function streamChat(prompt) {
  const stream = await client.chat.completions.create({
    model: MODEL,
    messages: [{ role: "user", content: prompt }],
    stream: true,
  });
  for await (const chunk of stream) {
    const delta = chunk.choices?.[0]?.delta?.content;
    if (delta) process.stdout.write(delta);
  }
  console.log();
}

const prompt = "用一句话解释什么是向量数据库";
console.log("=== 普通调用 ===");
console.log(await simpleChat(prompt));

console.log();
console.log("=== 流式调用 ===");
await streamChat(prompt);
