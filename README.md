# ChainControl

一个面向物联网设备控制的 Python 项目。

## 当前可用能力
- `backend_service.py`：后端 HTTP 服务，提供 `GET /health` 与 `POST /control`。
- `desktop_assistant.py`：桌面端小助手（Tkinter），通过 HTTP 调用后端服务。
- `PROJECT_ANALYSIS.md`：项目目标、差距与演进路线分析。

## 快速开始（后端 + 桌面端）
1. 启动后端：
   ```bash
   uvicorn backend_service:app --host 0.0.0.0 --port 8000
   ```
2. 启动桌面端：
   ```bash
   python desktop_assistant.py
   ```
3. 在桌面助手中：
   - 配置服务地址（默认 `http://127.0.0.1:8000`）
   - 点击“健康检查”验证连通性
   - 输入控制命令并发送

## 接口约定
- `GET /health`
- `POST /control`

### /control 请求示例
```json
{
  "command": "打开客厅灯",
  "context": {}
}
```

### /control 响应示例
```json
{
  "ok": true,
  "answer": "已为你打开客厅灯"
}
```
