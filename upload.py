# upload.py
import os
import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_youtube_service(account: str):
    token_file = f"token_{account}.pickle"
    creds = None
    if os.path.exists(token_file):
        with open(token_file, "rb") as f:
            creds = pickle.load(f)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open(token_file, "wb") as f:
            pickle.dump(creds, f)

    return build("youtube", "v3", credentials=creds)

def upload(file_path: str, account: str, title: str, description: str, tags: list = None):
    try:
        youtube = get_youtube_service(account)
        media = MediaFileUpload(file_path, mimetype="video/mp4", resumable=True, chunksize=8*1024*1024)

        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": title,
                    "description": description,
                    "tags": tags or ["shorts", "viral", "励志", "motivation"],
                    "categoryId": "22"
                },
                "status": {"privacyStatus": "public"}
            },
            media_body=media
        )

        print(f"[UPLOAD] 开始上传 → {title} 到 {account}")
        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"    → {int(status.progress() * 100)}% 已上传")

        print(f"[SUCCESS] 上传完成！视频ID: {response['id']}  | 标题: {title}")
        return response

    except HttpError as e:
        print(f"[ERROR] YouTube API 错误 ({account}): {e.status_code}")
        raise
    except Exception as e:
        print(f"[ERROR] 上传失败: {e}")
        raise
