import subprocess
import time
import os
from tkinter import Tk, Canvas, mainloop

WIDTH, HEIGHT, ZOOM = 256, 64, 3

window = Tk()
canvas = Canvas(window, width=WIDTH*ZOOM, height=HEIGHT*ZOOM, bg="#000000")

while 1:

   x=0;y=0
   b=[]

   canvas.delete("all")
   canvas.pack()

   with open(os.devnull, 'w')  as FNULL:
      subprocess.run(["sudo", "dd","if=/dev/fb0","of=./display","bs=1","count=16384"], stdout=FNULL, stderr=subprocess.STDOUT)

   time.sleep(1)

   f=open("./display","rb")

   for byte in f:
      b.extend(byte)

   for i in range(0, len(b)):
      x+=1
      if (x % WIDTH) == 0:
         x=0;y+=1
      if b[i] > 0:
         canvas.create_rectangle( (x, y)*2 , outline='#003333')
      if b[i] > 16:
         canvas.create_rectangle( (x, y)*2 , outline='#004444')
      if b[i] > 32:
         canvas.create_rectangle( (x, y)*2 , outline='#005555')
      if b[i] > 48:
         canvas.create_rectangle( (x, y)*2 , outline='#006666')
      if b[i] > 64:
         canvas.create_rectangle( (x, y)*2 , outline='#007777')
      if b[i] > 80:
         canvas.create_rectangle( (x, y)*2 , outline='#008888')
      if b[i] > 96:
         canvas.create_rectangle( (x, y)*2 , outline='#00aaaa')
      if b[i] > 112:
         canvas.create_rectangle( (x, y)*2 , outline='#66ffff')
      if b[i] > 128:
         canvas.create_rectangle( (x, y)*2 , outline='#77ffff')
      if b[i] > 144:
         canvas.create_rectangle( (x, y)*2 , outline='#88ffff')
      if b[i] > 160:
         canvas.create_rectangle( (x, y)*2 , outline='#99ffff')
      if b[i] > 176:
         canvas.create_rectangle( (x, y)*2 , outline='#aaffff')
      if b[i] > 192:
         canvas.create_rectangle( (x, y)*2 , outline='#bbffff')
      if b[i] > 208:
         canvas.create_rectangle( (x, y)*2 , outline='#ccffff')
      if b[i] > 224:
         canvas.create_rectangle( (x, y)*2 , outline='#ddffff')
      if b[i] > 240:
         canvas.create_rectangle( (x, y)*2 , outline='#ffffff')

   canvas.scale("all", 0, 0, ZOOM, ZOOM)
   canvas.configure(scrollregion = canvas.bbox("all"))

   window.update_idletasks()
   window.update()

#mainloop()
