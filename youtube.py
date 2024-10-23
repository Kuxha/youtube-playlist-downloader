import yt_dlp

def download_youtube_playlist(playlist_url):
    ydl_opts = {
        'format': 'best', # for donwaldoing the bres quality
        'outtmpl': '%(title)s.%(ext)s', # basically save all files 
        'progress_hooks': [hook],  # shows you the progerss of the downlaod
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def hook(d):
    if d['status'] == 'finished':
        print(f"\nDone downloading: {d['filename']}")

if __name__ == '__main__':
    # add your own youtube playlist url here
    playlist_url = 'https://www.youtube.com/playlist?list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj'
    download_youtube_playlist(playlist_url)
