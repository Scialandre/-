from pytube import YouTube
from moviepy.editor import VideoFileClip,AudioFileClip
from sys import *
import os
import subprocess

from private_var import *


mode=argv[2]
link = argv[1]
forbiddenChar=('<','>',':','"','/','\\','|','?','*')


try:
    yt = YouTube(link)
    titolo = yt.title  #trovare il modo di strippare caratteri strani
    for character in forbiddenChar:
        titolo = titolo.replace(character,'')

except:
    if mode!='i':
        print('errore di apertura link')

def main():

    if mode!='i':
        vidInfo()
    else:
        print('SYTDL - Scialandre YouTube DownLoader')




    if mode == 'd':
        stitchDownload()
    if mode == 'pd':
        progressiveDowload()
    if mode == 'ad':
        audioDowload()




def vidInfo():
    print(f'Titolo\t\t{yt.title}')
    if titolo!=yt.title and mode in ('d','pd','ad'):
        print(f'Nome File\t{titolo}')
    print(f'Autore\t\t{yt.author}\t{yt.channel_url}')
    print(f'Durata\t\t{yt.length}')
    print(f'Views\t\t{yt.views}')
    print(f'Pubblicato\t{yt.publish_date}')

def stitchDownload():
    try:
        #ydv= yt.streams.filter(progressive=False,file_extension='mp4').order_by("resolution").last()
        ydv = yt.streams.get_by_itag(137)
        yda = yt.streams.get_by_itag(140)

        ydv.download(output_path=outputFolder,filename_prefix='video-',filename=f'{titolo}.mp4')
        yda.download(output_path=outputFolder,filename_prefix='audio-',filename=f'{titolo}.mp4')
        print(f'dowloaded stream video:{ydv}')
        print(f'dowloaded stream audio:{yda}')


    except:
        print('errore di download')

    try:
        finalVideo = VideoFileClip(f'{outputFolder}video-{titolo}.mp4')
        audioclip = AudioFileClip(f'{outputFolder}audio-{titolo}.mp4')
        finalVideo = finalVideo.set_audio(audioclip)
        finalVideo.write_videofile(f'{outputFolder}{titolo}.mp4')
        print('file scaricato correttamente')
    except:
        print('errore di editing')

def progressiveDowload():

    try:
        yd=yt.streams.filter(file_extension='mp4').get_highest_resolution()
        yd.download(output_path=outputFolder,filename=f'{titolo}.mp4')
        print('progressive download completo')
    except:
        print('errore di download')

def audioDowload():

    try:
        yd=yt.streams.get_by_itag(139)
        yd.download(output_path=outputFolder,filename=f'{titolo}.mp4')
        #print('')

        #video_file,ext = os.path.splitext(f'{outputFolder}\\{titolo}.mp4')
        #print(video_file,'cccc',ext)


        #subprocess.call(["ffmpeg","-y","-i",video_file,f"{video_file}.mp3"],
                        #stdout=subprocess.DEVNULL,
                        #stderr=subprocess.STDOUT)

        print('audio download completo')
    except:
        print('errore di download')


if __name__ == "__main__":
    main()