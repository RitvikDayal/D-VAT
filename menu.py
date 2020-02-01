# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:53:49 2020

@author: Cyber Lord
"""
from tkinter import *
import tkinter.messagebox

bg_color = '#394b5c'


'''-------------------------------Window Configuration----------------------------------------'''
root = Tk()
root.title('Data Visualizer and Analyzer')
root.iconbitmap(r'icon.ico')
root.config(bg=bg_color)
root.resizable(width=False, height=False)
root.geometry('850x400+450+150')


#========================================================================================================================

'''-------------------------TITLE_LABEL-------------------------------------------------------'''
fr1 = Frame(root, bg=bg_color, width=489, height=318)
fr1.grid(columnspan=10, sticky=W, padx=20, pady=40)

img_main = PhotoImage(file = "img_main.png")

background_label = Label(fr1, image=img_main, relief=RIDGE, bd=10 )
background_label.grid()

'''-------------------------Buttons-------------------------------------------------------'''

fr2 = Frame(root, bg=bg_color, width=350, height=350)
fr2.grid(row=0, column=12,sticky=N, padx=5, pady=40)

btn_1 = Button(fr2, bg="#3c85fa", fg="white", activebackground="#33ff74", height=2, width=20, text="Visualizer", bd=5, font=('arial',16,'bold'))
btn_1.grid(row=0, sticky=N, pady=15)

btn_2 = Button(fr2, bg="#3c85fa", fg="white", activebackground="#33ff74", height=2, width=20, text="Analyzer", bd=5, font=('arial',16,'bold'))
btn_2.grid(row=1, sticky=N, pady=15)

btn_3 = Button(fr2, bg="#3c85fa", fg="white", activebackground="#33ff74", height=2, width=20, text="Coder", bd=5, font=('arial',16,'bold'))
btn_3.grid(row=2, sticky=N, pady=15)

dev_msg = Label(fr2, fg="white", bg=bg_color, text="Devloped by: Ritvik Dayal", font=('arial',10,'italic'))
dev_msg.grid(row=3, sticky=SE)
'''---------------------Main Loop------------------------------------------------------'''
root.mainloop()
