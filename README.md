Video Farm

Video Farm 是一个自动化视频生成与上传工具，用于批量生成视频并上传到 YouTube 频道。

该项目主要用于：

自动生成视频内容

自动上传视频

多账号轮换上传

自动化内容生产流程


适用于在 Termux / Linux / macOS 等环境运行。


---

Features

自动生成视频

自动上传到 YouTube

支持多个频道

自动轮换频道上传

自动生成标题

上传状态日志



---

Project Structure

video_farm/

├── farm.py

├── upload.py

├── client_secret.json

├── generated_videos/

├── token_acc1.pickle

├── token_acc2.pickle

└── README.md

说明：

文件	作用

farm.py	主程序，生成视频并上传
upload.py	YouTube 上传模块
client_secret.json	Google OAuth 凭证
generated_videos	自动生成的视频
token_acc1.pickle	频道1登录 token
token_acc2.pickle	频道2登录 token



---

Requirements

Python 3.9+

安装依赖：

pip install google-api-python-client
pip install google-auth-oauthlib

Termux 用户：

pkg install python
pip install google-api-python-client google-auth-oauthlib


---

Setup

1 获取 YouTube API

打开：

https://console.cloud.google.com/

创建项目：

启用

YouTube Data API v3

创建 OAuth Client ID

下载：

client_secret.json

放入项目目录。


---

2 账号授权

第一次运行时会自动打开浏览器授权。

python3 farm.py

授权后会生成：

token_acc1.pickle
token_acc2.pickle

以后不会再次要求登录。


---

Running

运行：

python3 farm.py

流程：

生成视频
↓

保存到 generated_videos
↓

选择账号
↓

上传 YouTube

日志示例：

[INFO] Generated video video_A1B2C3.mp4
[INFO] Uploaded video_A1B2C3.mp4 to acc1


---

Multiple Channels

在 farm.py 中配置：

ACCOUNTS = ["acc1", "acc2"]

系统会：

视频1 → acc1
视频2 → acc2
视频3 → acc1
视频4 → acc2

循环上传。


---

Custom Video Generation

默认示例为简单视频生成。

你可以替换：

generate_video()

使用：

AI 视频生成

图片转视频

文本转视频

自动剪辑


实现自己的内容生产流程。


---

Notes

请确保 YouTube API 已启用

账号需要拥有 YouTube 频道

上传频率过高可能触发平台限制



---

License

MIT License
