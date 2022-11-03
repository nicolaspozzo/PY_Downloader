
from pytube import YouTube

url = input("Enter url: ")
youtube_video = YouTube(url)

print('Tittle: ', youtube_video.title)
print('Views: ', youtube_video.views)

download_video = youtube_video.streams.get_highest_resolution()
download_path = "./Downloads"

try:
    download_video.download(download_path) # folder path to download the video
except:
    print("Error")

print("Video downloaded successfully")
