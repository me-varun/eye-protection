# import tkinter as tk
# from PIL import ImageTk,Image
# import time

# #Setting Dimensions of the window

# w = 700
# h = 350

# #  Loading Image 

# image = Image.open("index.jpg")
# image = image.resize((w,h))



# class main():

#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry('%dx%d+0+0' % (w,h))
#         self.photo = ImageTk.PhotoImage(image)
#         self.bg_img = tk.Label(self.root,image = self.photo)
#         self.root.resizable(False,False)
#         self.lbl1 = tk.Label(self.root,text="Time",font=('forte',20)) 
#         self.t = tk.StringVar()
#         self.t.set("00:00:00")
#         self.time = tk.Label(self.root,textvariable=self.t,font=('forte',30))
#         self.libo = tk.Listbox(self.root,height=3)
#         self.libo.insert(1,"20-20")
#         self.libo.insert(2,"30-20")
#         self.libo.insert(1,"30-30")
#         print(self.libo.curselection())

#         self.libo.pack(side="bottom")
        
#         self.bg_img.place(relwidth=1,relheight=1)
#         self.lbl1.place(relx= 0.03,rely = 0.05, relwidth = 0.3 , relheight = 0.2 )
#         self.time.place(relx= 0.35,rely = 0.05, relwidth = 0.4 , relheight = 0.2)

#         self.root.mainloop()


# # root = tk.Tk()

# # #============================

# # root.wm_attributes('-transparentcolor','red')

# # #============================
# # i=0
# # def change():
# #     global i
# #     i = i+1
# #     t.set("yeh"+str(i))
# #     root.after(960,change)
    

# # t = tk.StringVar()
# # t.set("00:00:00")

# # root.geometry('%dx%d+0+0' % (w,h))


# # #canvas  = tk.Canvas(root,width=500 , height=250 , bg ='blue').place(relx= 0,rely = 0, relwidth = 1 , relheight = 1)
# # frame = tk.Frame(root,bg="red").place(relx= 0,rely = 0, relwidth = 1 , relheight = 1)

# # bg_label = tk.Label(root,image=photo).place(relx= 0,rely = 0, relwidth = 1 , relheight = 1)

# # lbl1 = tk.Label(root,text="Time Remaining :",font=("forte",15))
# # lbl1.place(relx= 0.05,rely = 0.05, relwidth = 0.3 , relheight = 0.2)
# # #Button 1
# # bt1 = tk.Button(frame,textvariable=t,command= lambda:change()).place(relx= 0.5,rely = 0.1, relwidth = 0.3 , relheight = 0.1)

# # root.resizable(False,False)

# # root.mainloop()

# a = main()
#--------------------------------------------------------------------------------------------------
from PyQt5 import QtCore

def start_timer(slot, count,min_,sec ,interval=1000):
    counter = 0
    print(min_,sec,end="-->")
    def handler():
        nonlocal counter
        counter += 1
        slot(counter)
        if counter >= count:
            timer.stop()
            timer.deleteLater()
    timer = QtCore.QTimer()
    timer.timeout.connect(handler)
    timer.start(interval)

def timer_func(count):
    print('Timer:', count)
    if count >= 5:
        QtCore.QCoreApplication.quit()

app = QtCore.QCoreApplication([])
min_ = 1
sec = 20
start_timer(timer_func,5,min_,sec)
app.exec_()
