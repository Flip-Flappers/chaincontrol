# ChainControl

一个面向物联网设备控制的 Python 项目。

## 当前可用能力
- `desktop_assistant.py`：桌面端小助手（Tkinter），用于通过 HTTP 调用后端服务。
- `PROJECT_ANALYSIS.md`：项目目标、差距与演进路线分析。

## 桌面端小助手使用方式
1. 启动你的后端服务（需提供以下接口）：
   - `GET /health`
   - `POST /control`
2. 启动桌面助手：
   ```bash
   python desktop_assistant.py
   ```
3. 在桌面助手中：
   - 配置服务地址（默认 `http://127.0.0.1:8000`）
   - 点击“健康检查”验证连通性
   - 输入控制命令并发送

## /control 请求示例
```json
{
  "command": "打开客厅灯",
  "context": {}
}
```

## /control 响应示例
```json
{
  "ok": true,
  "answer": "已为你打开客厅灯"
}
```
