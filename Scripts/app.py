# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from app_fun import predict_captcha
from app_fun2 import randomString


class ocr_app(tk.Tk):
    def __init__(self,parent):
       tk.Tk.__init__(self,parent)
       self.parent = parent
       self.initialize()
      
    def initialize(self):
        self.grid()
        
        self.message = tk.Label( self, text = "Generate new Captcha by clicking on 'Generate'" )
        self.message.grid(column = 1,row = 0)
        
        
        im = Image.open('canvas.jpg')
        tkimage = ImageTk.PhotoImage(im)
        self.myCanvas=tk.Label(self, image=tkimage)
        self.myCanvas.image = tkimage
        self.myCanvas.grid(column = 1,row = 1)
        
        self.button = tk.Button(self,text="Generate",command = self.generate)
        self.button.grid(column=2,row=1)
        
        self.var = tk.StringVar()
        
        self.predicted = tk.Label(self, textvariable=self.var)
        self.var.set("Click Predict to break the Captcha!")
        self.predicted.grid(column = 1, row = 2)
        
        self.button = tk.Button(self,text = "Predict", command = self.prediction)
        self.button.grid(column = 2,row = 2)
    
     
    def generate(self):
        randomString()
        im2 = Image.open('canvas.jpg')
        new_image = ImageTk.PhotoImage(im2)
        self.myCanvas.config(image=new_image)
        self.myCanvas.image = new_image
        self.var.set("Click Predict to break the Captcha!")
        self.predicted.config(font=("Helvetica", 9))
   
        
    
    def prediction(self):
        y = predict_captcha('canvas.jpg')
        self.var.set(y)
        self.predicted.config(font=("Helvetica", 14))
   

if __name__ == "__main__":
    app = ocr_app(None)
    app.title('CAPTCHA Recognizer')
    app.mainloop()
