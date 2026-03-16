# farm.py
import os
import random
import string
import time
import subprocess
from upload import upload

ACCOUNTS = ["acc1", "acc2"]
VIDEO_FOLDER = "./generated_videos"
os.makedirs(VIDEO_FOLDER, exist_ok=True)
os.makedirs("./fonts", exist_ok=True)   # 放 NotoSansSC-Regular.ttf

# 爆款标题模板（播放量神器）
TITLE_TEMPLATES = [
    "💥 {quote} 99%的人都忽略了！🔥 #shorts",
    "震惊！这个习惯让你{benefit}！🚀 2026必看",
    "🔥 每天坚持这个，30天彻底改变人生！💪",
    "你知道吗？{quote} 太扎心了…😭 #viral",
    "99%的人不知道！{quote} 快收藏！📌",
    "🚨 2026最新秘诀：{quote} 直接起飞！",
    "太燃了！{quote} 看完直接行动！🔥",
    "别刷了！先看这个：{quote} 改变从现在开始",
]

BENEFIT_LIST = ["月入翻倍", "身材暴瘦", "自信爆棚", "效率翻10倍"]

# 励志文案（视频里显示的文字）
QUOTES = [
    "坚持梦想，你会成功！",
    "每天进步1%，一年改变人生！",
    "你比自己想象的更强大！",
    "失败只是通往成功的弯路",
    "现在不努力，未来会后悔一辈子",
    "行动起来！机会只给有准备的人",
    "相信自己，你已经很棒了！",
    "每一天都是新的开始！"
]

def generate_high_quality_shorts(file_path: str):
    quote = random.choice(QUOTES)
    benefit = random.choice(BENEFIT_LIST)
    title = random.choice(TITLE_TEMPLATES).format(quote=quote, benefit=benefit)
    
    # 高质量竖版 Shorts 生成命令（音乐+字幕+高画质）
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", "color=c=black:s=1080x1920:d=15",   # 15秒竖版
        "-stream_loop", "-1", "-i", "bg_music.mp3",             # 循环音乐
        "-vf", f"drawtext=fontfile=fonts/NotoSansSC-Regular.ttf:fontsize=85:fontcolor=white:box=1:boxcolor=black@0.6:x=(w-text_w)/2:y=(h-text_h)/2:text='{quote}'",
        "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",                                            # 跟视频时长一致
        file_path
    ]
    
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[GENERATED] 高质量 Shorts 生成完成 → {title}")
        return title, f"{quote}\n\n自动生成励志短视频\n每天更新更多爆款！\n#YouTubeShorts #励志 #motivation #viral #shorts"
    except Exception as e:
        print(f"[FFMPEG 错误] 请确认 ffmpeg 已安装且 bg_music.mp3、字体存在！{e}")
        raise

def cleanup(file_path: str):
    try:
        os.remove(file_path)
        print(f"[CLEAN] 已删除临时视频")
    except:
        pass

def main():
    print("🚀 YouTube Shorts 自动农场已启动！无限模式运行中...")
    video_count = 0
    
    while True:
        fname = f"shorts_{''.join(random.choices(string.ascii_letters + string.digits, k=8))}.mp4"
        file_path = os.path.join(VIDEO_FOLDER, fname)

        title, description = generate_high_quality_shorts(file_path)
        account = ACCOUNTS[video_count % 2]

        try:
            upload(file_path, account, title, description)
            cleanup(file_path)
            video_count += 1
            print(f"📈 第 {video_count} 个视频上传成功！继续冲播放量...")
        except Exception as e:
            print(f"[FAIL] 上传失败，继续下一个")

        # 随机延时 30\~60 分钟（自然增长 + 防风控）
        sleep_time = random.randint(1800, 3600)
        print(f"⏳ 休息 {sleep_time//60} 分钟后继续...")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()
