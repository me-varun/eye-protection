import tkinter as tk
from PIL import ImageTk,Image

w = 500
h = 250

root = tk.Tk()

#============================

root.wm_attributes('-transparentcolor','white')

#============================


root.geometry('%dx%d+0+0' % (w,h))

image = Image.open("index.jpg")
image = image.resize((w,h))
photo = ImageTk.PhotoImage(image)

#canvas  = tk.Canvas(root,width=500 , height=250 , bg ='blue').place(relx= 0,rely = 0, relwidth = 1 , relheight = 1)
frame = tk.Frame(root,bg="red").place(relx= 0,rely = 0, relwidth = 1 , relheight = 1)

bg_label = tk.Label(root,image=photo).place(relx= 0,rely = 0, relwidth = 1 , relheight = 1)

lbl1 = tk.Label(frame,text="Time Remaining :",bg='black',font=("forte",30))
lbl1.pack(side="top")
#Button 1
tk.Button(frame,text="Stop").place(relx= 0,rely = 0.1, relwidth = 0.3 , relheight = 0.5)

root.resizable(False,False)

root.mainloop()

