import os
import re
import tkinter as tk
from tkinter import messagebox, ttk
from yt_dlp import YoutubeDL

def sanitize_filename(name):
    """
    Sanitize the filename by replacing invalid characters with underscores.
    Invalid characters for Windows directories: \\ / : * ? " < > |
    """
    invalid_chars = r'[\\\/:*?"<>|]'
    return re.sub(invalid_chars, '_', name)

def parse_ranges(range_str, total_videos):
    """
    Parse the user's range input (e.g., '1-52' or '1-20,30-52') into a list of 1-based indices.
    """
    parts = range_str.split(',')
    indices = set()
    for part in parts:
        part = part.strip()
        if '-' in part:
            start_end = part.split('-')
            if len(start_end) != 2:
                raise ValueError(f"Invalid range format: {part}")
            try:
                start = int(start_end[0])
                end = int(start_end[1])
            except ValueError:
                raise ValueError(f"Range must contain numbers: {part}")
            start = max(1, start)
            end = min(total_videos, end)
            for i in range(start, end + 1):
                indices.add(i)
        else:
            try:
                num = int(part)
            except ValueError:
                raise ValueError(f"Invalid number: {part}")
            if 1 <= num <= total_videos:
                indices.add(num)
    return sorted(indices)

def get_playlist_info(playlist_url):
    """
    Retrieve the playlist title and total number of videos using yt-dlp.
    """
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        return info['title'], len(info['entries'])

def download_videos(playlist_url, indices, directory, quality, format_type, mp3_quality, progress_var, status_var):
    """
    Download the specified videos from the playlist using yt-dlp with selected quality and format.
    """
    quality_map = {
        '360p': 'bestvideo[height<=360]+bestaudio/best[height<=360]',
        '480p': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
        '720p': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        '1080p': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        '2k': 'bestvideo[height<=1440]+bestaudio/best[height<=1440]',
        '4k': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
    }
    
    ydl_opts = {
        'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
        'playlist_items': ','.join(map(str, indices)),
        'retries': 3,
        'quiet': False,
        'ignoreerrors': True,
        'progress_hooks': [lambda d: update_progress(d, progress_var, status_var)],
    }
    
    if format_type == 'mp3':
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': mp3_quality,
        }]
    elif format_type == 'mp4':
        if quality in quality_map:
            ydl_opts['format'] = quality_map[quality]
        else:
            print(f"Invalid quality selected. Defaulting to best available.")
            ydl_opts['format'] = 'bestvideo+bestaudio/best'
        ydl_opts['merge_output_format'] = 'mp4'
    else:
        print(f"Invalid format selected. Defaulting to MP4.")
        ydl_opts['format'] = 'bestvideo+bestaudio/best'
        ydl_opts['merge_output_format'] = 'mp4'
    
    with YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([playlist_url])
        except Exception as e:
            print(f"Unexpected error during download: {e}")

def update_progress(d, progress_var, status_var):
    if d['status'] == 'downloading':
        progress_var.set(d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100)
        status_var.set(f"Downloading: {d.get('filename', 'Unknown')}")
    elif d['status'] == 'finished':
        status_var.set(f"Completed: {d.get('filename', 'Unknown')}")
    elif d['status'] == 'error':
        status_var.set(f"Error: {d.get('error', 'Unknown error')}")

def start_download():
    playlist_link = playlist_entry.get()
    range_str = range_entry.get()
    quality = quality_var.get()
    format_type = format_var.get().lower()
    mp3_quality = mp3_quality_var.get() if format_type == 'mp3' else '192'
    
    try:
        playlist_title, total_videos = get_playlist_info(playlist_link)
        selected_indices = parse_ranges(range_str, total_videos)
        if not selected_indices:
            messagebox.showerror("Error", "No videos selected to download.")
            return
        directory = os.path.join("D:/", "Video", sanitize_filename(playlist_title))
        os.makedirs(directory, exist_ok=True)
        download_videos(playlist_link, selected_indices, directory, quality, format_type, mp3_quality, progress_var, status_var)
        messagebox.showinfo("Success", "Download process completed.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("YouTube Playlist Downloader")

tk.Label(root, text="Playlist Link:").grid(row=0, column=0, pady=5)
playlist_entry = tk.Entry(root, width=50)
playlist_entry.grid(row=0, column=1, pady=5)

tk.Label(root, text="Range (e.g., '1-52'):").grid(row=1, column=0, pady=5)
range_entry = tk.Entry(root, width=50)
range_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="Quality:").grid(row=2, column=0, pady=5)
quality_var = tk.StringVar(value='720p')
quality_options = ['360p', '480p', '720p', '1080p', '2k', '4k']
quality_menu = tk.OptionMenu(root, quality_var, *quality_options)
quality_menu.grid(row=2, column=1, pady=5)

tk.Label(root, text="Format:").grid(row=3, column=0, pady=5)
format_var = tk.StringVar(value='MP4')
format_options = ['MP4', 'MP3']
format_menu = tk.OptionMenu(root, format_var, *format_options)
format_menu.grid(row=3, column=1, pady=5)

tk.Label(root, text="MP3 Quality (if applicable):").grid(row=4, column=0, pady=5)
mp3_quality_var = tk.StringVar(value='192')
mp3_quality_options = ['128', '192', '320']
mp3_quality_menu = tk.OptionMenu(root, mp3_quality_var, *mp3_quality_options)
mp3_quality_menu.grid(row=4, column=1, pady=5)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100, length=300)
progress_bar.grid(row=5, column=0, columnspan=2, pady=5, sticky='ew')

status_var = tk.StringVar()
status_label = tk.Label(root, textvariable=status_var, wraplength=400)
status_label.grid(row=6, column=0, columnspan=2, pady=5)

download_button = tk.Button(root, text="Start Download", command=start_download)
download_button.grid(row=7, column=0, columnspan=2, pady=5)

root.mainloop()
