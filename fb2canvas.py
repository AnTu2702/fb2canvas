import subprocess
import time
import os
from tkinter import Tk, Canvas, mainloop

WIDTH, HEIGHT, VWIDTH, VHEIGHT, SCALE, ZOOM = 144, 64, 512, 256, 3, 2

window = Tk()
window.geometry(f"{ZOOM*WIDTH*SCALE}x{ZOOM*HEIGHT*SCALE}")
canvas = Canvas(window, width=VWIDTH*ZOOM, height=VHEIGHT*ZOOM, bg="#000000")

x=0;y=0
b=[]

canvas.delete("all")
canvas.pack()
canvas.place(x=-(VWIDTH-WIDTH*SCALE)*ZOOM, height=(VHEIGHT-HEIGHT)*ZOOM)

# with open("jolly_8bit.bmp", "rb") as image:
#     f = image.read()
#     b = bytearray(f)

#     with open("jolly_8bit_prep.bmp", "wb") as output:
#         output.write(b)

f=open("./screenshot","rb")

for byte in f:
    b.extend(byte)

for i in range(VWIDTH*VHEIGHT*0, int(len(b)>>0), 1): #complete images is already in first 512*256 bytes

    x+=1
    if (x % VWIDTH) == 0:
        x=0;y+=1

    if b[i] == 0:
        canvas.create_rectangle( (x, y)*2 , outline='#000000')
    else:
        canvas.create_rectangle( (x, y)*2 , outline='#ff9900')

    # if 16 > b[i] >= 0:
    #     canvas.create_rectangle( (x, y)*2 , outline='#003333')
    # elif 32 > b[i] >= 16:
    #     canvas.create_rectangle( (x, y)*2 , outline='#004444')
    # elif 48 > b[i] >= 32:
    #     canvas.create_rectangle( (x, y)*2 , outline='#005555')
    # elif 64 > b[i] >= 46:
    #     canvas.create_rectangle( (x, y)*2 , outline='#006666')
    # elif 80 > b[i] >= 63:
    #     canvas.create_rectangle( (x, y)*2 , outline='#007777')
    # elif 96 > b[i] >= 80:
    #     canvas.create_rectangle( (x, y)*2 , outline='#008888')
    # elif 112 > b[i] >= 96:
    #     canvas.create_rectangle( (x, y)*2 , outline='#00aaaa')
    # elif 128 > b[i] >= 112:
    #     canvas.create_rectangle( (x, y)*2 , outline='#66ffff')
    # elif 144 > b[i] >= 128:
    #     canvas.create_rectangle( (x, y)*2 , outline='#77ffff')
    # elif 160 > b[i] >= 144:
    #     canvas.create_rectangle( (x, y)*2 , outline='#88ffff')
    # elif 176 > b[i] >= 160:
    #     canvas.create_rectangle( (x, y)*2 , outline='#99ffff')
    # elif 192 > b[i] >= 176:
    #     canvas.create_rectangle( (x, y)*2 , outline='#aaffff')
    # elif 208 > b[i] >= 192:
    #     canvas.create_rectangle( (x, y)*2 , outline='#bbffff')
    # elif 224 > b[i] >= 208:
    #     canvas.create_rectangle( (x, y)*2 , outline='#ccffff')
    # elif 240 > b[i] >= 224:
    #     canvas.create_rectangle( (x, y)*2 , outline='#ddffff')
    # else:
    #     canvas.create_rectangle( (x, y)*2 , outline='#ffffff')

canvas.scale("all", 1, 1, ZOOM, ZOOM)
canvas.configure(scrollregion = canvas.bbox("all"))

window.update_idletasks()
window.update()

mainloop()