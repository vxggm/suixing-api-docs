# 客户端配置

多数支持「自定义 API 地址」的客户端都能接，填两个值即可：

| 字段 | 值 |
|---|---|
| API 地址 / Base URL | `https://api.ns666.cfd/v1` |
| API Key | 控制台创建的令牌 |

## Cherry Studio

设置 → 模型服务 → 添加 → 类型选 OpenAI → 填地址与 Key → 添加模型 `deepseek-v4-flash`

## ChatBox

设置 → 模型 → API 类型选 OpenAI API → API 域名填 `https://api.ns666.cfd` → 填 Key

## LobeChat

设置 → 语言模型 → OpenAI → 接口代理地址填 `https://api.ns666.cfd/v1` → 填 Key

## NextChat

设置 → 自定义接口 → 接口地址填 `https://api.ns666.cfd` → 填 Key

## 通用注意

- 地址结尾**不要**多加斜杠
- 模型名必须与控制台里的一致
- Key 泄露立即在控制台删除并重建
