from tkinter import *
import os 
os.system('clear')

root = Tk()
root.title('Test GUI App')
root.geometry("400x200")

myLabel =Label(root, text='Enter your name: ')
myLabel.pack()

  

root.mainloop()