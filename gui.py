import tkinter as tk
from tkinter import messagebox




class sytdlGui:
    
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("1000x900")
        self.fonto = ('Arial, 18')

        self.label = tk.Label(self.root, text="SYTDL", font=self.fonto)
        self.label.pack(padx=10,pady=10)

        self.linkLabel = tk.Label(self.root, text="link")
        self.linkLabel.pack()

        self.linktextbox = tk.Text(self.root, height=1, font=self.fonto)
        self.linktextbox.pack(padx=10,pady=10)

        self.check = tk.Checkbutton(self.root, text="aaaaaa",font=self.fonto)
        self.check.pack(padx=10,pady=10)

        self.buttono = tk.Button(self.root,text="bbbbb",font=self.fonto,command=self.buttonFunc)
        self.buttono.pack(padx=10,pady=10)

        self.root.mainloop() 

        

    def buttonFunc(self):
        messagebox.showinfo(title='link',message=self.linktextbox.get('1.0',tk.END))
        link = self.linktextbox.get('1.0',tk.END)
        

       