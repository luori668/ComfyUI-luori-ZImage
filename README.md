# ComfyUI-luori-ZImage

一个专为 **Z-Image**（造相 / Z-Image Turbo）模型优化的 ComfyUI 自定义节点插件。

让 Z-Image 在 ComfyUI 中使用更方便、更强大，支持更好的提示词处理。

添加了一个工作流。

# 增加了Krea-2的lora填充窗口
  新增一个穿搭预设选择器

## ✨ 使用方法
插件更新后 删除画布内插件重新添加

comfyUI画布内 双击搜索 落日  即可


## ✨ 主要功能

- 支持 Z-Image Turbo base Qwen klein 提示词的快速生成
- 优化后的提示词处理节点 速度更快
  
- 删除 NSFW 测试版节点

- 动作与姿势描述

- ✨ Z-image-落日-提示词抽取器，新增超强模式，
 
-  超强模式新增提示词超400W字符，15000组提示词（超级推荐）

 
## 📦 安装方法

### 方法一：使用 ComfyUI Manager（推荐）
1. 在 ComfyUI 中打开 **Manager**
2. 点击 **Install Custom Nodes**
3. 搜索 `luori-ZImage` 或 `ComfyUI-luori-ZImage`
4. 安装后重启 ComfyUI

5.<img width="1437" height="790" alt="f8914655-2b6d-4060-a933-b828702c6df3" src="https://github.com/user-attachments/assets/a2941b0c-9b04-4b3c-bc8c-83a2be227622" />






### 方法二：手动安装
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/piaoling44/ComfyUI-luori-ZImage.git
cd ComfyUI-luori-ZImage
pip install -r requirements.txt
