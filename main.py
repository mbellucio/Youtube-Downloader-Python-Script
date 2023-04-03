from pytube import YouTube

url = 'https://www.youtube.com/watch?v=lmc21V-zBq0'

youtube = YouTube(url)
video = youtube.streams.get_highest_resolution()
video.download('./Downloads')



