import os
import whisper
import torch
from yt_dlp import YoutubeDL
from tqdm import tqdm
# 检查GPU是否可用
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using {device} device")

# 加载Whisper模型（选择适合你的模型大小）
model = whisper.load_model("medium").to(device) #turbo

def set_proxy(proxy_url):
    """
    设置系统代理
    :param proxy_url: 代理地址，例如 'http://127.0.0.1:1080'
    """
    os.environ['http_proxy'] = proxy_url
    os.environ['https_proxy'] = proxy_url
    print(f"Proxy set to: {proxy_url}")

def download_youtube_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',  # 使用视频标题作为文件名
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'cookiefile': 'cookies.txt',  # 使用导出的cookies文件
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info_dict)  # 获取生成的文件名
        # 创建以视频标题命名的文件夹
        folder_name = info_dict['title']
        os.makedirs(folder_name, exist_ok=True)
        # 移动下载的文件到新文件夹
        new_path = os.path.join('result',folder_name, filename.rsplit('.', 1)[0] + '.mp3')
        os.rename(filename.rsplit('.', 1)[0] + '.mp3', new_path)
        return new_path

def transcribe_audio(file_path):
    # 使用Whisper进行转录
    result = model.transcribe(
        file_path,
        # task="translate",
        verbose=True
        )
     # 添加详细进度条
    with tqdm(total=len(result['segments']), desc="转录进度", unit="segment") as pbar:
        for segment in result['segments']:
            pbar.set_postfix({
                'start': f"{segment['start']:.1f}s",
                'end': f"{segment['end']:.1f}s"
            })
            pbar.update(1)
    
    return result["text"]

def youtube_to_text(url):
    # 下载音频并转录
    audio_path = download_youtube_audio(url)
    text = transcribe_audio(audio_path)
    # 获取文件夹路径
    folder_path = os.path.dirname(audio_path)
    transcription_name = os.path.splitext(os.path.basename(audio_path))[0]
    # 保存转录结果到文件
    output_file = os.path.join(folder_path, f"{transcription_name}.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"\n转录结果已保存到: {output_file}")

if __name__ == "__main__":
    # 设置代理（根据需要修改或注释掉）
    set_proxy('http://127.0.0.1:10802')  #

    youtube_url = input("请输入YouTube视频URL: ")
    transcription = youtube_to_text(youtube_url)
    print("\n转录结果：")
    print(transcription)