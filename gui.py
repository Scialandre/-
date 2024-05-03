import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import os
from PIL import ImageTk, Image
import requests
from io import BytesIO




class sytdlGui:

    videoTitle ="Link"
    thumbnailUrl = ""
    
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("1000x900")
        self.titleFont = ('Arial', 18)
        self.Font=('Arial',16)

        self.label = tk.Label(self.root, text="SYTDL", font=self.titleFont)
        self.label.pack(padx=10,pady=10)

        self.linkLabel = tk.Label(self.root, text=self.videoTitle, font=self.Font)
        self.linkLabel.pack()

        self.thumbnailLabel = tk.Label(self.root)
        self.thumbnailLabel.pack(fill="both")

        self.linktextbox = tk.Text(self.root, height=1, font=self.Font)
        self.linktextbox.pack(padx=10,pady=10)

        

        self.SDbutton = tk.Button(self.root,text="Stitch Download",font=self.Font,command=self.buttonFunc)
        self.SDbutton.pack(padx=10,pady=10)

        self.PDbutton = tk.Button(self.root,text="Progressive Download",font=self.Font,command=self.buttonFunc)
        self.PDbutton.pack(padx=10,pady=10)

        self.ADbutton = tk.Button(self.root,text="Audio Download",font=self.Font,command=self.buttonFunc)
        self.ADbutton.pack(padx=10,pady=10)

        self.root.mainloop() 

        

    def buttonFunc(self):
        
        link = self.linktextbox.get('1.0',tk.END)
        self.videoTitle=YouTube(link).title
        img_url = YouTube(link).thumbnail_url

        response = requests.get(img_url)
        img_data = response.content

        img= ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

        self.linkLabel.config(text=self.videoTitle)
        self.thumbnailLabel.config(image=img,width=320,height=180)

        messagebox.showinfo(title='link',message=self.videoTitle)
        
        #self.linktextbox.delete('1.0',tk.END)
        

       