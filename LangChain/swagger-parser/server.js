const express = require('express');
const SwaggerParser = require('@apidevtools/swagger-parser');
const OpenAPISampler = require('openapi-sampler');
const path = require('path');

const app = express();
const port = 3000;

// Swagger JSON 文件路径
const swaggerFilePath = path.join(__dirname, 'swagger.json');

// 解析并缓存 Swagger 文档
let apiSpec = null;
async function loadSwagger() {
  try {
    apiSpec = await SwaggerParser.dereference(swaggerFilePath);
    console.log('Swagger 文件解析成功');
  } catch (error) {
    console.error('解析 Swagger 失败:', error.message);
  }
}
loadSwagger(); // 服务器启动时加载 Swagger 文件

// 获取 API 详情
app.get('/api/details', async (req, res) => {
  const { path, method } = req.query;

  if (!apiSpec) {
    return res.status(500).json({ error: 'Swagger 文件未成功加载' });
  }

  if (!path || !method) {
    return res.status(400).json({ error: '缺少 path 或 method 参数' });
  }

  const operation = apiSpec.paths?.[path]?.[method.toLowerCase()];
  if (!operation) {
    return res.status(404).json({ error: '接口不存在或方法错误' });
  }

  res.json({
    summary: operation.summary || '无描述',
    description: operation.description || '无描述',
    parameters: operation.parameters || [],
  });
});

// 新增 openapi-sampler 独立接口
// `openapi-sampler` 独立接口，接受 JSON Schema 生成示例数据
app.post('/api/sample', (req, res) => {
  const schema = req.body;

  if (!schema || typeof schema !== 'object') {
    return res.status(400).json({ error: '请求体必须是有效的 JSON Schema 对象' });
  }

  try {
    // 生成示例数据
    const example = OpenAPISampler.sample(schema, { skipReadOnly: true });
    res.json(example);
  } catch (error) {
    res.status(500).json({ error: `生成示例数据失败: ${error.message}` });
  }
});

// 启动服务器
app.listen(port, () => {
  console.log(`API 服务器已启动:
- 获取接口详情: http://localhost:${port}/api/details?path=/user&method=post
- 生成 Schema 示例: http://localhost:${port}/api/sample?schemaPath=components.schemas.User`);
});
