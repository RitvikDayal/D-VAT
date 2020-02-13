from tkinter import filedialog
from tkinter import *
bg_color = '#394b5c'

def fileSelection():
	file_path =  filedialog.askopenfilename(initialdir = "/",title = "Select file")
	print(file_path)

root = Tk()
root.title('Data Visualizer and Analyzer')
root.iconbitmap(r'icon.ico')
root.config(bg=bg_color)
root.resizable(width=False, height=False)
root.geometry('850x100+450+150')

btn = Button(root, bg="#3c85fa", fg="white", activebackground="#33ff74", width=20, text="Choose Data File", bd=5, font=('arial',16,'bold'), padx = 10, command = fileSelection)
btn.pack()

root.mainloop()