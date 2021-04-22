import sys 
import tkinter

  
mygui = tkinter.Tk() 
  
mygui.geometry('450x450+500+300')  
mygui.title('my tkinter') 
 
count = 0  
  
def add(): 
    global count  
    count += 1 
    print (count) 
button = tkinter.Button(text = 'add 1',command = add ).pack() 

mygui.mainloop()