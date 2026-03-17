# resources_manager.py
import os
import subprocess
import random
from moviepy.editor import VideoFileClip

# 目录
BACKGROUND_DIR = "backgrounds"
MUSIC_DIR = "music"
os.makedirs(BACKGROUND_DIR, exist_ok=True)
os.makedirs(MUSIC_DIR, exist_ok=True)

# YouTube 链接列表，可以是频道或播放列表
HOT_CHANNELS = [
    "https://www.youtube.com/shorts_channel_or_playlist_url1",
    "https://www.youtube.com/shorts_channel_or_playlist_url2"
]

# 每个频道下载的视频数量
NUM_VIDEOS = 5

def is_vertical(video_path):
    """判断视频是否竖版"""
    try:
        clip = VideoFileClip(video_path)
        return clip.h > clip.w
    except Exception as e:
        print(f"[WARN] 无法读取视频 {video_path}: {e}")
        return False

def download_shorts(url, max_items=5):
    """使用 yt-dlp 下载指定频道/播放列表的 Shorts"""
    cmd = [
        "yt-dlp",
        "-f", "mp4",
        "-o", os.path.join(BACKGROUND_DIR, "%(title)s.%(ext)s"),
        "--playlist-items", f"1-{max_items}",
        url
    ]
    print(f"[INFO] 下载 Shorts: {url}")
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] 下载失败: {e}")

def filter_vertical_videos():
    """删除 backgrounds/ 中非竖版视频"""
    for file in os.listdir(BACKGROUND_DIR):
        path = os.path.join(BACKGROUND_DIR, file)
        if path.lower().endswith(".mp4") and not is_vertical(path):
            print(f"[INFO] 删除非竖版视频: {file}")
            os.remove(path)

def fetch_hot_backgrounds():
    """下载并筛选热门背景视频"""
    for url in HOT_CHANNELS:
        download_shorts(url, NUM_VIDEOS)
    filter_vertical_videos()
    print(f"[INFO] 下载完成，剩余竖版视频数量: {len(os.listdir(BACKGROUND_DIR))}")

def get_random_background():
    """随机返回一个背景视频路径"""
    files = [f for f in os.listdir(BACKGROUND_DIR) if f.lower().endswith(".mp4")]
    if not files:
        print("[ERROR] backgrounds/ 目录没有视频，请先下载")
        return None
    return os.path.join(BACKGROUND_DIR, random.choice(files))

def get_random_music():
    """随机返回一个音乐文件路径"""
    files = [f for f in os.listdir(MUSIC_DIR) if f.lower().endswith(".mp3")]
    if not files:
        print("[WARN] music/ 目录没有音乐，使用默认 bg_music.mp3")
        default_path = os.path.join(MUSIC_DIR, "bg_music.mp3")
        return default_path if os.path.exists(default_path) else None
    return os.path.join(MUSIC_DIR, random.choice(files))

if __name__ == "__main__":
    fetch_hot_backgrounds()
    print(f"[INFO] 示例随机背景: {get_random_background()}")
    print(f"[INFO] 示例随机音乐: {get_random_music()}")
