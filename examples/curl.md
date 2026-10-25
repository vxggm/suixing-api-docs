# curl 速查

## 基础调用

```bash
curl https://api.ns666.cfd/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $SUIXING_API_KEY" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "你好"}]
  }'
```

## 流式输出

```bash
curl -N https://api.ns666.cfd/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $SUIXING_API_KEY" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [{"role": "user", "content": "写一段介绍"}],
    "stream": true
  }'
```

`-N` 关闭 curl 缓冲，否则看不到逐字输出。

## 列出模型

```bash
curl https://api.ns666.cfd/v1/models \
  -H "Authorization: Bearer $SUIXING_API_KEY"
```

## 只看响应头与耗时

```bash
curl -o /dev/null -s -w "状态:%{http_code} 耗时:%{time_total}s\n" \
  https://api.ns666.cfd/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $SUIXING_API_KEY" \
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"hi"}]}'
```

## 错误码

| 码 | 含义 | 处理 |
|---|---|---|
| 401 | Key 无效 | 检查 Authorization 头 |
| 403 | 令牌禁用/额度耗尽 | 登录控制台 |
| 404 | 路径写错 | 使用 `/v1/chat/completions` |
| 429 | 触发限流 | 降低频率、加退避 |
| 500 | 上游异常 | 重试 |
