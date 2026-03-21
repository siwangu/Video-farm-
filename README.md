# 🌾 Video Farm

> Automated video generation & multi-channel YouTube upload tool

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![YouTube API](https://img.shields.io/badge/YouTube%20API-v3-red?style=flat-square&logo=youtube)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Termux-lightgrey?style=flat-square)

---

## 📌 Overview

**Video Farm** is an automated pipeline for batch-generating videos and uploading them to YouTube channels with zero manual intervention.

Designed for:
- 🎬 Automated video content generation
- 🚀 Automatic video uploads to YouTube
- 🔄 Multi-account rotation uploads
- ⚙️ Fully automated content production workflows

Runs on **Termux** · **Linux** · **macOS**

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎬 Auto Video Generation | Batch-produce videos with pluggable generation backends |
| 🚀 Auto YouTube Upload | Push videos via YouTube Data API v3 |
| 🔄 Account Rotation | Distribute uploads across multiple channels |
| ✏️ Auto Title Generation | Dynamically generate titles at upload time |
| 📋 Upload Logging | Structured logs for every upload event |
| 📱 Termux Compatible | Runs fully on Android — no desktop required |

---

## 📁 Project Structure

```
video_farm/
│
├── farm.py                 # Main program: generates and uploads videos
├── upload.py               # YouTube upload module
├── client_secret.json      # Google OAuth credentials
│
├── generated_videos/       # Output directory for generated videos
│
├── token_acc1.pickle       # OAuth token for channel 1
├── token_acc2.pickle       # OAuth token for channel 2
│
└── README.md
```

---

## ⚙️ Requirements

Python **3.9+** is required.

**Standard (Linux / macOS)**
```bash
pip install google-api-python-client google-auth-oauthlib
```

**Termux (Android)**
```bash
pkg install python
pip install google-api-python-client google-auth-oauthlib
```

---

## 🚀 Setup

### 1. Obtain YouTube API Credentials

1. Open [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project
3. Enable **YouTube Data API v3**
4. Create an **OAuth Client ID**
5. Download `client_secret.json` and place it in the project root

### 2. Authorize Accounts

On first run, a browser window opens for OAuth authorization:

```bash
python3 farm.py
```

After authorization, token files are saved automatically:

```
token_acc1.pickle
token_acc2.pickle
```

> ✅ Subsequent runs reuse these tokens — no login required.

---

## ▶️ Running

```bash
python3 farm.py
```

### Workflow

```
🎬 Generate Video
      ↓
💾 Save to generated_videos/
      ↓
🔄 Select Account (rotation)
      ↓
🚀 Upload to YouTube
```

### Example Log Output

```
[INFO] Generated video video_A1B2C3.mp4
[INFO] Uploaded video_A1B2C3.mp4 → acc1
```

---

## 📡 Multiple Channels

Configure your accounts in `farm.py`:

```python
ACCOUNTS = ["acc1", "acc2"]
```

Uploads rotate evenly across all accounts:

| Video | Account |
|---|---|
| Video 1 | acc1 |
| Video 2 | acc2 |
| Video 3 | acc1 |
| Video 4 | acc2 |

---

## 🛠️ Custom Video Generation

A basic `generate_video()` example is included. Replace it with any backend:

```python
# Replace generate_video() with your own backend:
# - AI video generation
# - Image-to-video
# - Text-to-video
# - Auto-editing pipeline
# - Any custom content production workflow
```

---

## ⚠️ Notes

- Ensure **YouTube Data API v3** is enabled in your Google Cloud project
- Each account must have an active **YouTube channel**
- Excessive upload frequency may trigger **API quota limits** — upload responsibly

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution.

---

<div align="center">
  <sub>🌾 Video Farm — Automated YouTube Content Pipeline</sub>
</div>
