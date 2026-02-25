# ChainControl

一个面向物联网设备控制的 Python 项目。

## 当前可用能力
- `backend_service.py`：后端 HTTP 服务，提供 `GET /health` 与 `POST /control`。
- `desktop_assistant.py`：桌面端小助手（Tkinter），通过 HTTP 调用后端服务。
- `PROJECT_ANALYSIS.md`：项目目标、差距与演进路线分析。

## 快速开始（单入口启动）
```bash
python run_desktop_with_backend.py
```

默认会自动启动后端（`http://127.0.0.1:8000`）并打开桌面助手。

如需自定义端口：
```bash
python run_desktop_with_backend.py --host 127.0.0.1 --port 8001
```

## 快速开始（手动分开启动）
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
   - 设置用户ID并输入控制命令发送（同一用户并发请求会被后端拒绝）

## 接口约定
- `GET /health`
- `POST /control`

### /control 请求示例
```json
{
  "command": "打开客厅灯",
  "user_id": "alice",
  "context": {}
}
```

### /control 响应示例
```json
{
  "ok": true,
  "user_id": "alice",
  "answer": "已为你打开客厅灯",
  "raw": {
    "steps": [
      {"name": "加载执行器", "status": "completed", "detail": "已加载 Swagger pipeline", "duration_ms": 10},
      {"name": "执行命令解析", "status": "completed", "detail": "命令解析与工具选择完成", "duration_ms": 280}
    ]
  }
}
```


## 并发约束（按用户隔离）
- 后端基于 `user_id` 做并发控制：同一 `user_id` 在一个命令处理完成前，新的 `/control` 请求会返回 `409`。
- 不同 `user_id` 之间可以并行发送命令。
- 桌面端会在本地请求处理中禁用“发送命令”按钮，避免重复提交。


## 步骤可视化
- 后端会在 `/control` 响应的 `raw.steps` 返回每一步的 `name/detail/status/duration_ms`。
- 桌面端会在聊天窗口中按顺序显示“请求准备 -> 调用后端 -> 后端步骤详情 -> 最终结果”。
