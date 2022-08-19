from turtle import title
from pytube import YouTube

url = input("Informe a URL do vídeo que deseja baixar: ")

video = YouTube(url)

video.streams.get_highest_resolution().download(
    output_path = r"C:\Users\Kurumí\Downloads\intesivopy",
    filename = video.title
)
#video.streams.filter(only_audio=True).first().download(
#    output_path = "C:/Users/Kurumí/Downloads/intesivopy",
#    filename = video.title + ".mp3")