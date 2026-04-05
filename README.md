# ComfyUI-luori-ZImage

一个专为 **Z-Image**（造相 / Z-Image Turbo）模型优化的 ComfyUI 自定义节点插件。

让 Z-Image 在 ComfyUI 中使用更方便、更强大，支持更好的提示词处理、采样控制、LoRA 加载等功能。

## ✨ 主要功能

- 支持 Z-Image Turbo 快速生成
- 优化后的提示词处理节点（兼容 Qwen3-4B chat template）
- 便捷的 LoRA 加载与权重控制
- 专用采样节点（支持低显存优化）
- 工作流模板（example_workflows 文件夹）

## 📦 安装方法

### 方法一：使用 ComfyUI Manager（推荐）
1. 在 ComfyUI 中打开 **Manager**
2. 点击 **Install Custom Nodes**
3. 搜索 `luori-ZImage` 或 `ComfyUI-luori-ZImage`
4. 安装后重启 ComfyUI

### 方法二：手动安装
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/piaoling44/ComfyUI-luori-ZImage.git
cd ComfyUI-luori-ZImage
pip install -r requirements.txt
