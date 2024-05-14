from pytube import YouTube
from moviepy.editor import VideoFileClip,AudioFileClip
from sys import *
import os

from SYTLDlogger import *
from private_var import *

global link
global mode

forbiddenChar=('<','>',':','"','/','\\','|','?','*','.')
titolo=''
yt = ''



def main():

    print('SYTDL - Scialandre YouTube DownLoader')
    setup()
    
    
    if mode == 'h':
        helpMessage()
    else:
        vidInfo()
        modeDispatch()
    

def setup():
    global yt, mode, link, titolo

    try:
        mode = argv[2]
        link = argv[1]
    except:
        logger.error('Argomenti insufficienti')

    try:
        yt = YouTube(link)
        titolo= yt.title
        try:
            for character in forbiddenChar:
                titolo = titolo.replace(character,'')
        except:
            logger.error('Errore strip titolo')
    except:
        logger.error('Errore apertura link')

    try:
        yt.bypass_age_gate()
    except:
        logger.error('Errore bypass_age_gate()')

def modeDispatch():
    if mode == 'd':
        stitchDownload()
    elif mode == 'pd':
        progressiveDowload()
    elif mode == 'ad':
        audioDowload()
    elif mode == 'i':
        pass
    else:
        logger.error('Modalità inesistente')

def vidInfo():
    global titolo

    print(f'Titolo\t\t{yt.title}')
    if titolo!=yt.title:
        print(f'Nome File\t{titolo}.[extension]')
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
        

        cmd = f'{ffmpegDir}ffmpeg.exe -y -i \"{outputFolder}{titolo}.mp4\" \"{outputFolder}{titolo}.mp3\"'
        #subprocess.call(cmd,shell=True)
        os.system(cmd)

        print('audio download completo')
    except:
        print('errore di download')

def helpMessage():
    print('Argomenti/Modalità:')
    print('d-\tStitch Download, lento ma qualità migliore (lascia file residui)')
    print('pd-\tProgressive Download, veloce ma qualità inferiore')
    print('ad-\tAudio Download, solo audio (crea file mp3 ed mp4)')
    print('i-\tMostra info video')
    print('h-\tMostra questo messaggio')

if __name__ == "__main__":
    main()