import os, re
import tkinter as tk

from moviepy import editor as mp
from pytube import Playlist, YouTube
from tkinter import filedialog as fd
  
def baixar(playlist):
    print("\n" + "Informe a pasta de download: ")
    root = tk.Tk()
    root.withdraw()
    destino = fd.askdirectory()

    print("--> Baixando...")
    
    contador = 0
    
    for url in playlist:
        try:
            YouTube(url).streams.first().download(destino)
        except:
            contador += 1
            continue

    if contador > 0:
        if contador == 1:
            print("\n" + str(contador) + " vídeo não pôde ser baixado!")

        else:
            print("\n" + str(contador) + " vídeos não puderam ser baixados!")
    
    print("\n" + "--> Convertendo...")
    
    for arquivo in os.listdir(destino):
        if re.search('mp4', arquivo):
            mp4_path = os.path.join(destino, arquivo)
            mp3_path = os.path.join(destino, os.path.splitext(arquivo)[0] + '.mp3')
            novo = mp.AudioFileClip(mp4_path)
            novo.write_audiofile(mp3_path)
            os.remove(mp4_path)

    print("\n" + "Processo concluído! Obrigado!")
                                
print("\n" + "--> Bem-vindo ao Baixação (MP3PL Edition)!" + "\n")
url = input("Informe a URL da playlist: ")
playlist = Playlist(url)

if not playlist:
    print("A playlist não pôde ser acessada!")

else:
    baixar(playlist)
  



    
