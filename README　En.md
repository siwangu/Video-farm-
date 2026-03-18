

Video Farm

Video Farm is an automated video generation and upload tool designed to batch-create videos and upload them to YouTube channels.

This project is primarily designed for:

Automated video content generation

Automatic video uploads

Multi-account rotation for uploads

Fully automated content production workflows


It can run on Termux / Linux / macOS environments.


---

Features

Automatic video generation

Upload videos to YouTube automatically

Support for multiple channels

Rotating upload between accounts

Automatic title generation

Upload status logging



---

Project Structure

video_farm/
│

├── farm.py

├── upload.py

├── client_secret.json

│

├── generated_videos/

│

├── token_acc1.pickle

├── token_acc2.pickle


└── README.md

Description of files:

File	Purpose

farm.py	Main program, generates and uploads videos
upload.py	YouTube upload module
client_secret.json	Google OAuth credentials
generated_videos	Directory where generated videos are saved
token_acc1.pickle	OAuth token for channel 1
token_acc2.pickle	OAuth token for channel 2





Requirements

Python 3.9+


Install dependencies:

pip install google-api-python-client
pip install google-auth-oauthlib

For Termux users:

pkg install python
pip install google-api-python-client google-auth-oauthlib




Setup

1. Obtain YouTube API credentials

Open: Google Cloud Console

Create a project

Enable YouTube Data API v3

Create OAuth Client ID

Download client_secret.json and place it in the project directory





2. Account Authorization

On first run, the program will open a browser for authorization:


python3 farm.py

After authorization, tokens will be generated:


token_acc1.pickle
token_acc2.pickle

Subsequent runs will not require login again.




Running

Run the program:

python3 farm.py

Workflow:

Generate video

↓

Save to generated_videos

↓

Select account

↓

Upload to YouTube

Example log:

[INFO] Generated video video_A1B2C3.mp4
[INFO] Uploaded video_A1B2C3.mp4 to acc1




Multiple Channels

Configure in farm.py:


ACCOUNTS = ["acc1", "acc2"]

The system will rotate uploads:


Video 1 → acc1
Video 2 → acc2
Video 3 → acc1
Video 4 → acc2




Custom Video Generation

By default, a simple video generation example is provided.

You can replace generate_video() with:

AI video generation

Image-to-video

Text-to-video

Auto-editing


Implement your own content production workflow.



---

Notes

Make sure YouTube API is enabled

The accounts must have a YouTube channel

Excessive upload frequency may trigger platform limits





License

MIT License
