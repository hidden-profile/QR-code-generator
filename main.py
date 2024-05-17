#to build  qrcode there are modules pyqrcode and pillow
from tkinter import *
import pyqrcode
from PIL import ImageTk, Image 
def qrcode():
    n=ne.get()
    l=le.get()
    #generate image file with name entry
    file=n+".png"
    url=pyqrcode.create(l)
    url.png(file,scale=8)
    #png not worked for this pip install pypng
    # Image.open(file)
    #opening image but not displaying
    #for displaying we use PhotoImage in ImageTk
    img=ImageTk.PhotoImage(Image.open(file))
    imgl=Label(root,image=img)
    imgl.image=img
    canvas.create_window(200,450,window=imgl)
    #qrcode generated and saved in system

root=Tk()
canvas=Canvas(root,width=400,height=700)
canvas.pack()
l=Label(root,text="QR Code Generator",fg='blue',font=("Arail",30))
canvas.create_window(200,50,window=l)
name=Label(root,text="Link Name")
link=Label(root,text="Link URL")
ne=Entry(root)
le=Entry(root)
canvas.create_window(200,100,window=name)
canvas.create_window(200,160,window=link)
canvas.create_window(200,130,window=ne)
canvas.create_window(200,190,window=le)
btn=Button(text="Generate Qr code",command=qrcode)
canvas.create_window(200,230,window=btn)
root.mainloop()