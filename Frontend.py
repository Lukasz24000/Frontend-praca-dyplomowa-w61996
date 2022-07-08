#-------------------------------------------------------------------------------
import math
import numpy
import os
from decimal import *
#Python 3.x:
from tkinter import *
from tkinter import filedialog
#-------------------------------------------------------------------------------
def openfile1():
    #funkcja do otwierania pliku (okno dialogowe):
    file=e1.get()
    e1.delete(0, END)
    filename=filedialog.askopenfilename(title="Select file 1:")
    e1.insert(0,filename)
    if len(e1.get())==0:
        e1.insert(0,file)




root = Tk()
root.title("LSDyna material generator ")
CheckvarVector=[]
checkButtons=[]
#*****okna do wpisywania sciezek do pliku:**************


Up0Frame=LabelFrame(root)
Up0Frame.grid(row=0, column=1)

labelE1=Label(Up0Frame,text='Path:',font=("Arial 10 bold"))
labelE1.grid(row=0,column=0)
e1=Entry(Up0Frame,width = 60)
#sticky means that it will be glued to left (west=w) and right(east=e)
e1.grid(row=0, column=1)

button_file = Button(Up0Frame, text="...", command=openfile1)
button_file.grid(row=0, column=2)

canv = Canvas(root, width=1000, height=800, bg='white')
canv.grid(row=1, column=1, columnspan=2, rowspan = 3)

img = PhotoImage(file='powodz.gif')
canv.create_image(20,20, anchor=NW, image=img)





Left0Frame=LabelFrame(root)
Left0Frame.grid(row=1, column=0)


video_button = Button(Left0Frame, text="Analiza wideo", height = 1, width = 15, font=("Arial 10"), command=lambda: StreamAnalysis())
video_button.grid(row=1, column=0, columnspan=2)

image_button= Button(Left0Frame, text="Analiza obrazu", height = 1, width = 15, font=("Arial 10"), command=lambda: ImageAnalysis())
image_button.grid(row=2, column=0, columnspan=2)


button_start = Button(Left0Frame, text="Start Analizy", height = 1, width = 12, font=("Arial 12 bold"), command=lambda: startFunction())
button_start.grid(row=3, column=0, columnspan=2)


buttonleft = Button(Left0Frame, text="<",  font=("Arial 12 bold"))
buttonleft.grid(row=4, column=0)
buttonright = Button(Left0Frame, text=">",  font=("Arial 12 bold"))
buttonright.grid(row=4, column=1)

var1 = IntVar()
var2 = IntVar()
c1 = Checkbutton(Left0Frame, text='Dym',variable=var1)
c1.grid(row=5, column=0)
c2 = Checkbutton(Left0Frame, text='Ogien')
c2.grid(row=5, column=1)


root.mainloop()