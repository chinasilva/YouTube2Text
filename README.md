# YouTube 音频转录工具


[View English Version](README_EN.md)

## 项目简介
本工具可以将YouTube视频的音频下载并转录为文字，使用OpenAI的Whisper模型实现自动语音识别。

## 环境配置

### 1. 创建Python虚拟环境
bash
python -m venv venv
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install pytube openai-whisper


### 2. 获取YouTube Cookies
1. 在浏览器中安装EditThisCookie插件
2. 访问YouTube并登录
3. 导出cookies.json文件

[插件下载地址](https://chromewebstore.google.com/detail/editthiscookie/jpdpholcdjghlginfdaphhefdonkmohg?hl=en)

### 3. 转换Cookies格式
使用项目中的json2txt工具将cookies.json转换为cookies.txt

### 4. 运行转录工具
1. 修改代理设置（如果需要）：
python
在main.py中修改代理端口
set_proxy('http://127.0.0.1:10802') # 10802改为你的代理端口

2. 运行程序并输入YouTube视频地址：
bash
python convert.py
示例地址：
text
https://www.youtube.com/watch?v=eemgH5ZleQw


## 功能特点
- 自动创建以视频标题命名的文件夹
- 保存原始音频文件（MP3格式）
- 生成Markdown格式的转录文本
- 支持代理设置
- 支持Cookies登录

## 文件结构
项目目录/
├── 视频标题/
│ ├── 视频标题.mp3
│ └── 视频标题.md
├── cookies.txt
└── ...