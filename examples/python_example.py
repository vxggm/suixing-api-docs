#!/usr/bin/env python3
"""随性 API 调用示例

接口地址: https://api.ns666.cfd/v1
文档: https://blog.ns666.cfd
"""

import os
import time
from openai import OpenAI

API_KEY = os.environ.get("SUIXING_API_KEY", "your-key-here")
BASE_URL = "https://api.ns666.cfd/v1"
MODEL = "deepseek-v4-flash"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def simple_chat(prompt: str) -> str:
    """普通调用"""
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return resp.choices[0].message.content


def stream_chat(prompt: str) -> None:
    """流式调用"""
    stream = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()


def chat_with_retry(prompt: str, retries: int = 3) -> str:
    """带指数退避重试"""
    for i in range(retries):
        try:
            return simple_chat(prompt)
        except Exception as e:
            if i == retries - 1:
                raise
            wait = 2 ** i
            print(f"重试 {i + 1}/{retries}，{wait}s 后继续：{e}")
            time.sleep(wait)
    return ""


if __name__ == "__main__":
    print("=== 普通调用 ===")
    print(simple_chat("用一句话解释什么是 API 网关"))

    print()
    print("=== 流式调用 ===")
    stream_chat("用三句话介绍 Python 的异步编程")

    print()
    print("=== 带重试 ===")
    print(chat_with_retry("1+1 等于几？"))
