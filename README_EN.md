# YouTube to Text Transcription Tool


## [View Chinese Version](README.md)

## Overview
This tool allows you to download audio from YouTube videos and transcribe them into text using OpenAI's Whisper model.

## Environment Setup

### 1. Create Python Virtual Environment
bash
python -m venv venv
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install pytube openai-whisper


### 2. Get YouTube Cookies
1. Install EditThisCookie extension in your browser
2. Visit YouTube and log in
3. Export cookies.json file

[Extension Download Link](https://chromewebstore.google.com/detail/editthiscookie/jpdpholcdjghlginfdaphhefdonkmohg?hl=en)

### 3. Convert Cookies Format
Use the json2txt tool in the project to convert cookies.json to cookies.txt

### 4. Run Transcription Tool
1. Modify proxy settings (if needed):
python
Change proxy port in main.py
set_proxy('http://127.0.0.1:10802') # Change 10802 to your proxy port

2. Run the program and input YouTube video URL:
bash
python convert.py
https://www.youtube.com/watch?v=eemgH5ZleQw



## Features
- Automatically creates folder named after video title
- Saves original audio file (MP3 format)
- Generates transcription in Markdown format
- Supports proxy settings
- Supports cookies login

## File Structure
```
project_directory/
├── video_title/
│ ├── video_title.mp3
│ └── video_title.md
├── cookies.txt
└── ...