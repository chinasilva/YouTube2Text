
## 创建环境

1. 创建环境
***
    python -m venv venv
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
    pip install  pytube openai-whisper
***

2. 在浏览器中安装EditThisCookie插件，导出cookies.json
***
https://chromewebstore.google.com/detail/editthiscookie/jpdpholcdjghlginfdaphhefdonkmohg?hl=en
*** 
3. python json2txt 转换可用的cookies.txt

4. python convert.py代码    
    * 如果需要代理则在main中更改为本地代理端口,10802->1080
        ***
        set_proxy('http://127.0.0.1:10802')  ->
        ***
    * 输入youtube地址.例如:
        ***
        https://www.youtube.com/watch?v=eemgH5ZleQw 
        ***
