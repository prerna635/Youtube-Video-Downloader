import yt_dlp

def download_video(url):
    try:
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': '%(title)s.%(ext)s',  
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"\nDownloaded: {info['title']}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("YouTube Video Downloader (yt-dlp version) 🎬")
    video_url = input("Enter YouTube video URL: ")
    download_video(video_url)

