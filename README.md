# 随性 API · 低价快速的 DeepSeek 接入网关

> 兼容 OpenAI 协议的大模型 API 网关，把 DeepSeek 等模型的调用统一成一个标准接口。
> 一个 Key 通用，改一个 `base_url` 就能接入。

**官网**：https://www.ns666.cfd
**控制台**：https://api.ns666.cfd
**文档**：https://blog.ns666.cfd

---

## 为什么用它

| | |
|---|---|
| **零改动接入** | 标准 `/v1/chat/completions`，现有 SDK 只换 base_url |
| **流式输出** | SSE 逐字返回，首字延迟低 |
| **函数调用** | 支持 tool calling 与结构化输出 |
| **多模态** | 支持图片输入 |
| **用量管理** | 按 token 精确计量，多用户多分组 |
| **故障切换** | 渠道自动重试，上游抖动无感 |

---

## 快速开始

### 1. 获取 Key

访问 https://api.ns666.cfd 注册账号，在「令牌」页面创建 Key。

### 2. curl 测试

```bash
curl https://api.ns666.cfd/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "你好"}]
  }'
```

### 3. Python

```python
from openai import OpenAI

client = OpenAI(
    api_key="你的KEY",
    base_url="https://api.ns666.cfd/v1",
)

resp = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "你好"}],
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
  messages: [{ role: "user", content: "你好" }],
});
console.log(resp.choices[0].message.content);
```

### 5. 流式输出

```python
stream = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "讲个故事"}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content if chunk.choices else None
    if delta:
        print(delta, end="", flush=True)
```

---

## 可用模型与价格

单位：美元 / 每 100 万 tokens

| 模型 | 输入 | 输出 | 缓存读 |
|---|---|---|---|
| deepseek-v4-flash | $0.1430 | $0.5720 | $0.0500 |
| deepseek-v4.1-flash | $0.1599 | $0.3198 | $0.0500 |
| deepseek-flash | $0.4000 | $1.1000 | $0.2000 |

按量计费，无月费、无最低消费。

---

## 完整文档

接入教程都在文档站：

- [快速开始：5 分钟接入 DeepSeek](https://blog.ns666.cfd/quickstart-deepseek-api/)
- [Python 完整示例（含流式输出）](https://blog.ns666.cfd/python-deepseek-v4-flash/)
- [Node.js 接入教程](https://blog.ns666.cfd/nodejs-api-tutorial/)
- [curl 命令行示例与参数详解](https://blog.ns666.cfd/curl-api-examples/)
- [流式输出（SSE）原理与实现](https://blog.ns666.cfd/streaming-sse-guide/)

---

## 常见问题

**Q：需要改现有代码吗？**
不用。任何支持自定义 `base_url` 的 SDK 都能直接接入，包括 OpenAI 官方 SDK、LangChain、LlamaIndex、Dify 等。

**Q：支持哪些客户端？**
Cherry Studio、ChatBox、LobeChat、NextChat、OpenCat、AMA 问天等主流客户端都能配置自定义 API 地址使用。

**Q：Key 怎么保管？**
不要硬编码在代码里，用环境变量。前端直连会暴露 Key，生产环境应经由自己的后端中转。

**Q：额度用完了怎么办？**
登录控制台补充额度，或新建令牌分别管理不同项目用量。

---

## 技术栈

网关基于 [New API](https://github.com/QuantumNous/new-api)（AGPL-3.0）二次开发，上游项目由 QuantumNous 维护。

---

## 链接

- 官网：https://www.ns666.cfd
- 控制台：https://api.ns666.cfd
- 文档：https://blog.ns666.cfd
- 状态监测：https://api.ns666.cfd/status-monitor

---

## 许可

本仓库内容采用 MIT 许可。网关本体基于 New API（AGPL-3.0）。