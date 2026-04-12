# ComfyUI-luori-ZImage

一个专为 **Z-Image**（造相 / Z-Image Turbo）模型优化的 ComfyUI 自定义节点插件。

让 Z-Image 在 ComfyUI 中使用更方便、更强大，支持更好的提示词处理。

添加了一个工作流。

## ✨ 使用方法
插件更新后 删除画布内插件重新添加

comfyUI画布内 双击搜索 落日  即可


## ✨ 主要功能

- 支持 Z-Image Turbo 和 base Qwen klein 提示词的快速生成
- 优化后的提示词处理节点 速度更快
- 再次新增词库
- 再次优化逻辑性
- 新增年龄和身材菜单 不选择 不输出 默认无
- 新增背包选项 去掉默认状态下偶现背包的描述
- 新增一个节点
 
## 📦 安装方法

### 方法一：使用 ComfyUI Manager（推荐）
1. 在 ComfyUI 中打开 **Manager**
2. 点击 **Install Custom Nodes**
3. 搜索 `luori-ZImage` 或 `ComfyUI-luori-ZImage`
4. 安装后重启 ComfyUI
 <img width="2118" height="1022" alt="image" src="https://github.com/user-attachments/assets/62d2ce5c-a486-4ea5-97bd-fdf4435fbc27" />

### 方法二：手动安装
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/piaoling44/ComfyUI-luori-ZImage.git
cd ComfyUI-luori-ZImage
pip install -r requirements.txt
