# ComfyUI-WaaS-API

基于云扉 API 的 ComfyUI 图像生成节点集合。包含文生图、图生图等功能。

## 功能介绍

本项目提供三个主要节点，支持灵活的图像生成工作流：

1. **设置API Key 节点** - 管理和配置 API 密钥
2. **全能图片-文生图 节点** - 根据文本描述生成图像
3. **全能图片-图生图 节点** - 基于参考图像生成新图像

## 安装说明

1. 将此存储库克隆到 ComfyUI 的 `custom_nodes` 目录：
   ```bash
   cd ~/comfyui/ComfyUI/custom_nodes
   git clone https://github.com/aigate2024/comfyui-aigate-api.git
   ```

2. 重启 ComfyUI

## 节点说明

### 1. 设置API Key（Setting）

**用途**：配置和保存 API 密钥

**输入参数**：
- **apiKey** (必填)：你的云扉 API 密钥

**输出**：
- **STRUCT** (结构体)：包含 API 密钥信息的结构体，供其他节点使用

**使用说明**：
- 将此节点的输出连接到文生图或图生图节点的 `settings` 输入
- API 密钥会被安全地传递到其他节点

---

### 2. 全能图片-文生图（aigate_txt2img）

**用途**：根据文本描述生成图像

**输入参数**：
- **prompt** (必填)：图像描述文本，支持中文和英文
- **settings** (必填)：来自"设置API Key"节点的结构体
- **model** (必填)：选择使用的模型
- **aspect_ratio** (可选)：图像方向
  - `Free (自由比例)` - 系统自动决定
  - `Landscape (横屏)` - 16:9 宽屏
  - `Portrait (竖屏)` - 9:16 竖屏
  - `Square (方形)` - 1:1 正方形
- **image_size** (可选)：生成图像的尺寸
  - `1K` - 标准清晰度
  - `2K` - 高清晰度

**输出**：
- **image**：生成的图像，可连接到其他节点进行进一步处理
- **API Respond**：包含处理日志和 API 响应的文本信息

**使用场景**：
- 从文本描述创建独特的概念艺术
- 生成插图、背景图或设计素材
- 快速创建视觉内容原型

---

### 3. 全能图片-图生图（aigate_img2img）

**用途**：基于参考图像生成新图像，支持多张参考

**输入参数**：
- **prompt** (必填)：对生成图像的描述或修改指示
- **settings** (必填)：来自"设置API Key"节点的结构体
- **model** (必填)：选择使用的模型
- **aspect_ratio** (可选)：同文生图
- **image_size** (可选)：同文生图
- **image1** (必填)：第一张参考图像
- **image2-image10** (可选)：最多 9 张额外参考图像

**输出**：
- **image**：生成的图像
- **API Respond**：处理日志和 API 响应信息

**多参考图像功能**：
- 支持一次性输入最多 10 张参考图像
- 多张参考图像会一起发送给 API 作为风格参考
- 适用于需要混合多种风格或提供详细参考的场景
- 第一张图像(image1)为必填，其余可选

**使用场景**：
- 根据参考图像生成类似风格的新图像
- 图像风格转移
- 基于参考创建变体
- 多源素材融合

---

## API 密钥获取

1. 访问云扉 API 官方平台
2. 注册账户或登录
3. 在 API 密钥管理部分创建新密钥
4. 复制密钥到"设置 API Key"节点（无需每次重复输入）

## 项目架构

```
BaseImageGenerator.py
├── 共用方法
├── API 调用
├── 响应处理
└── 日志管理

ImageGeneratorTxt2img.py (继承)
└── 文生图特定逻辑

ImageGeneratorImg2img.py (继承)
└── 图生图特定逻辑 + 多图处理

SettingsNode.py
└── API 密钥配置
```

## 注意事项

- API 可能有使用限制或费用，请查阅官方文档
- 图像生成质量和速度取决于 API 服务状态和网络连接
- 参考图像会被发送到 API 服务器，请注意隐私
- API 密钥通过 HTTP Authorization header 安全传递
- 图像方向为建议参数，模型生成结果不一定完全按照要求

## 文件说明

- `BaseImageGenerator.py` - 基础类，包含所有共用方法
- `ImageGeneratorTxt2img.py` - 文生图节点实现
- `ImageGeneratorImg2img.py` - 图生图节点实现  
- `SettingsNode.py` - API 密钥设置节点
- `__init__.py` - 节点注册和映射
- `requirements.txt` - 项目依赖

## License

请查看 LICENSE 文件了解许可证信息