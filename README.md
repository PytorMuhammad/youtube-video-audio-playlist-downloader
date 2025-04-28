## Overview
The YouTube Playlist Downloader is a Python-based tool designed to simplify the process of downloading videos and audio from YouTube Video playlists. It features a user-friendly graphical user interface (GUI) built with Tkinter and leverages the powerful yt-dlp library for efficient downloading. This tool is ideal for users who want to archive playlists, create offline music libraries, or save educational content for later viewing.

## Key Features
Custom Range Selection: Download specific videos or ranges from a playlist (e.g., "1-10" or "1-5,15-20").

Format Flexibility: Choose between MP4 (video) and MP3 (audio) formats.
Quality Options: Select video resolutions (360p, 480p, 720p, 1080p, 2K, 4K) or audio bitrates (128kbps, 192kbps, 320kbps).
Intuitive GUI: Easy-to-use interface with input fields, dropdowns, a progress bar, and real-time status updates.
Organized Downloads: Automatically saves files in a sanitized, playlist-named folder (e.g., "D:/Video/Playlist_Title").
Error Handling: Displays user-friendly error messages for invalid inputs or download failures.
Progress Tracking: Monitors download progress with a dynamic progress bar and status label.


## Installation
To set up the YouTube Playlist Downloader on your local machine, follow these steps:

## Prerequisites
Python 3.6 or higher: Download and install from python.org.
Required Libraries: Install the necessary Python packages using pip:
pip install yt-dlp
Note: Tkinter is typically included with Python installations. If not, install it separately:
Windows: Usually pre-installed.
macOS: Install via brew install python-tk.
Linux: Use your package manager (e.g., sudo apt install python3-tk on Ubuntu).
FFmpeg: Required for audio extraction (MP3) and video merging. Download from ffmpeg.org and add it to your system PATH:
Windows: Extract FFmpeg and add the bin folder to your PATH in Environment Variables.
macOS/Linux: Install via package manager (e.g., brew install ffmpeg on macOS or sudo apt install ffmpeg on Ubuntu).


## Steps
Clone the Repository:
git clone https://github.com/ToheedSahar/youtube-video-audio-playlist-downloader.git
Navigate to the Project Directory:
cd youtube-video-audio-playlist-downloader
Run the Script:
python yt_music&video_playlist_dl.py
The GUI will launch, and you're ready to start downloading!

## Usage
Follow these steps to download videos or audio from a YouTube playlist:
Enter Playlist Link:
Copy the URL of a YouTube playlist (e.g., https://youtube.com/playlist?list=PLRbp0E2gpnlh0AIV) and paste it into the "Playlist Link" field.
Specify Range:
In the "Range" field, enter the video indices you want to download:
Examples:
1-10 (downloads videos 1 to 10)
1-5,15-20 (downloads videos 1 to 5 and 15 to 20)
3 (downloads only video 3)

## Select Quality:
Choose your preferred video quality from the "Quality" dropdown:
for MP4 format Options: 360p, 480p, 720p, 1080p, 2k, 4k
Note: Higher quality requires more storage and download time.

## Choose Format:
Select the output format from the "Format" dropdown:
MP4: Downloads videos with both video and audio.
MP3: Extracts audio only.
Set MP3 Quality (if applicable):
If you selected MP3, choose the audio bitrate from the "MP3 Quality" dropdown:
Options: 128 (low quality), 192 (medium quality), 320 (high quality) kbps.

## Start Download:
Click the "Start Download" button.
Monitor the progress bar and status label for real-time updates (e.g., "Downloading: Video_Title.mp4" or "Completed: Video_Title.mp3").
Check Output:
Downloads are saved in D:/Video/Playlist_Title/ (e.g., D:/Video/Top_Hits_2023/).
Filenames are sanitized to remove invalid characters, ensuring compatibility across systems.
Tip: If you encounter errors (e.g., invalid URL or range), a pop-up will guide you to correct the issue.

## Additional Features
Retry Mechanism: Automatically retries failed downloads up to 3 times for reliability.
Sanitized Filenames: Removes invalid characters (e.g., /, *, <) from filenames.
Dynamic Directory Creation: Creates the output folder if it doesn’t exist.
Real-Time Feedback: Progress bar and status updates keep you informed throughout the process.
Contribution & Support
This project is open-source and welcomes contributions! Here’s how you can get involved:

Contribute: Fork the repository, make improvements (e.g., add subtitle support, enhance GUI), and submit a pull request.
Report Issues: Open a GitHub Issue for bugs or feature requests.
Support: Star the repository to increase its visibility and help others discover it.
For questions or assistance, feel free to open an issue on the GitHub page.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute it, provided the original license and copyright notice are included. See the LICENSE file for details
