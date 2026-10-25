# Suixing API · Low-cost DeepSeek Gateway

> An OpenAI-compatible gateway for DeepSeek models.
> One key, one `base_url` change, zero code rewrite.

**Website**: https://www.ns666.cfd
**Console**: https://api.ns666.cfd
**Docs**: https://blog.ns666.cfd

---

## Why use it

| | |
|---|---|
| **Drop-in** | Standard `/v1/chat/completions`, works with any OpenAI SDK |
| **Streaming** | SSE token-by-token output, low TTFT |
| **Tool calling** | Function calling and structured output |
| **Multimodal** | Image input supported |
| **Metering** | Exact per-token accounting, multi-user, multi-group |
| **Failover** | Automatic retry and channel switching |

---

## Quickstart

### 1. Get a key

Sign up at https://api.ns666.cfd and create a token in the console.

### 2. curl

```bash
curl https://api.ns666.cfd/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "hello"}]
  }'
```

### 3. Python

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_KEY",
    base_url="https://api.ns666.cfd/v1",
)

resp = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "hello"}],
)
print(resp.choices[0].message.content)
```

### 4. Node.js

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.API_KEY,
  baseURL: "https://api.ns666.cfd/v1",
});

const resp = await client.chat.completions.create({
  model: "deepseek-v4-flash",
  messages: [{ role: "user", content: "hello" }],
});
console.log(resp.choices[0].message.content);
```

### 5. Streaming

```python
stream = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content if chunk.choices else None
    if delta:
        print(delta, end="", flush=True)
```

---

## Models and pricing

USD per 1M tokens.

| Model | Input | Output | Cache read |
|---|---|---|---|
| deepseek-v4-flash | $0.1430 | $0.5720 | $0.0500 |
| deepseek-v4.1-flash | $0.1599 | $0.3198 | $0.0500 |
| deepseek-flash | $0.4000 | $1.1000 | $0.2000 |

Pay-as-you-go. No subscription, no minimum spend.

---

## Documentation

- [Quickstart: DeepSeek in 5 minutes](https://blog.ns666.cfd/quickstart-deepseek-api/)
- [Python walkthrough with streaming](https://blog.ns666.cfd/python-deepseek-v4-flash/)
- [Node.js integration](https://blog.ns666.cfd/nodejs-api-tutorial/)
- [curl reference and parameters](https://blog.ns666.cfd/curl-api-examples/)
- [SSE streaming internals](https://blog.ns666.cfd/streaming-sse-guide/)

---

## Examples in this repo

- [`examples/python_example.py`](examples/python_example.py) — plain call, streaming, retry with backoff
- [`examples/node_example.mjs`](examples/node_example.mjs) — plain call and streaming
- [`examples/curl.md`](examples/curl.md) — curl cheatsheet and error codes
- [`docs/clients.md`](docs/clients.md) — desktop client setup

---

## FAQ

**Do I need to change my code?**
No. Any SDK supporting a custom `base_url` works: OpenAI SDK, LangChain, LlamaIndex, Dify, and others.

**Which clients are supported?**
Cherry Studio, ChatBox, LobeChat, NextChat, OpenCat, and any client with a custom API endpoint field.

**How should I store the key?**
Use an environment variable, never hardcode. Browser-side calls expose the key — proxy through your own backend in production.

---

## Built on

Gateway layer based on [New API](https://github.com/QuantumNous/new-api) (AGPL-3.0).

---

## License

MIT for the contents of this repository.
