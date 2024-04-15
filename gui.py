import tkinter as tk
from tkinter import messagebox




class sytdlGui:
    
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("1000x900")
        self.titleFont = ('Arial', 18)
        self.Font=('Arial',16)

        self.label = tk.Label(self.root, text="SYTDL", font=self.titleFont)
        self.label.pack(padx=10,pady=10)

        self.linkLabel = tk.Label(self.root, text="Link", font=self.Font)
        self.linkLabel.pack()

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
        messagebox.showinfo(title='link',message=self.linktextbox.get('1.0',tk.END))
        link = self.linktextbox.get('1.0',tk.END)
        self.linktextbox.delete('1.0',tk.END)
        

       