import tkinter as tk
from tkinter import messagebox, StringVar
import yt_dlp

class PlaylistDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Playlist Downloader")
        
        # URL Input
        self.url_label = tk.Label(root, text="Enter Playlist URL:")
        self.url_label.pack(pady=10)
        
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=10)

        # Download Button
        self.download_button = tk.Button(root, text="Download Playlist", command=self.download_playlist)
        self.download_button.pack(pady=10)

        # Progress Label
        self.progress_label = tk.Label(root, text="")
        self.progress_label.pack(pady=10)

    def download_playlist(self):
        playlist_url = self.url_entry.get()
        if not playlist_url:
            messagebox.showwarning("Input Error", "Please enter a valid playlist URL.")
            return

        self.progress_label.config(text="Downloading...")
        self.root.update()

        # Call the download function
        self.download_youtube_playlist(playlist_url)

    def download_youtube_playlist(self, playlist_url):
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(playlist_index)s - %(title)s.%(ext)s',  # Include the video number in the title
            'progress_hooks': [self.hook],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])

    def hook(self, d):
        if d['status'] == 'finished':
            self.progress_label.config(text=f"Done downloading: {d['filename']}")
            self.root.update()

if __name__ == '__main__':
    root = tk.Tk()
    app = PlaylistDownloader(root)
    root.mainloop()
