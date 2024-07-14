import yt_dlp

def download_video(url, save_path):
   ydl_opts = {
       'outtmpl': f'{save_path}/%(title)s.%(ext)s',
       'format': 'best'
   }

   with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([url])
           

url = "https://youtu.be/AAt7oJ7MIDQ?si=Se0HvPNP6NDM0DWR"

save_path = "E:\web series"

download_video(url, save_path)


