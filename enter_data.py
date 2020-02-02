"""
Created on Sat Feb  1 19:53:49 2020

@author: Cyber Lord
"""
from tkinter import *
import tkinter

bg_color = '#394b5c'


'''-------------------------------Window Configuration----------------------------------------'''
root = Tk()
root.title('Data Visualizer and Analyzer')
root.iconbitmap(r'icon.ico')
root.config(bg=bg_color)
root.resizable(width=False, height=False)
root.geometry('850x400+350+150')

'''-------------------------------Title Message-----------------------------------------------'''

fr1 = Frame(root, bg=bg_color, height=15, width=750)
fr1.grid(sticky=N, padx=10, pady=10)

title_label = Label(fr1, text="Specify your data file format.", font=('arial',18,'bold'), bd=5, bg=bg_color, fg='white', justify=CENTER, anchor="center")
title_label.grid(padx=250, pady=15, sticky=NSEW)

'''--------------------------------File Formats-----------------------------------------------'''


fr2 = Frame(root, bg='#9acbe3', bd=10, relief=GROOVE, height=250, width=750)
fr2.grid(row=1, column=0, columnspan=20, padx=30, pady=30)

#format options:

csv_btn = Radiobutton(fr2, indicatoron=0, bg='#ff3838', text='CSV(Comma Separated Values)', font=('arial',14,'bold'), value=1, activeforeground='green', width=25)
csv_btn.grid(padx=10, pady=10, sticky=NW, columnspan=3)

json_btn = Radiobutton(fr2, indicatoron=0, bg='#ff3838', text='JSON(JavaScript Object Notation)', font=('arial',14,'bold'), value=2, activeforeground='green', width=25)
json_btn.grid(row=1, padx=10, pady=10, sticky=NW, columnspan=3)

xlsx_btn = Radiobutton(fr2, indicatoron=0, bg='#ff3838', text='XLSX(Excel File)', font=('arial',14,'bold'), value=3, activeforeground='green', width=25)
xlsx_btn.grid(row=2, padx=10, pady=10, sticky=NW, columnspan=3)

html_btn = Radiobutton(fr2, indicatoron=0, bg='#ff3838', text='HTML(HTML File)', font=('arial',14,'bold'), value=4, activeforeground='green', width=25)
html_btn.grid(column=5, row=0, padx=20, pady=10, sticky=NW)

SQL_btn = Radiobutton(fr2, indicatoron=0, bg='#ff3838', text='DB(SQL Table)', font=('arial',14,'bold'), value=5, activeforeground='green', width=25)
SQL_btn.grid(column=5, row=1, padx=20, pady=10, sticky=NW)

pickle_btn = Radiobutton(fr2, indicatoron=0, bg='#ff3838', text='PICKLE(Pickle File)', font=('arial',14,'bold'), value=6, activeforeground='green', width=25)
pickle_btn.grid(column=5, row=2, padx=20, pady=10, sticky=NW)

'''------------------------------Submit & Cancel-----------------------------------------------'''

 

'''------------------------------Main Loop-----------------------------------------------------'''
root.mainloop()