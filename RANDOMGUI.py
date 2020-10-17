from tkinter import *

#window = object

window=Tk()
window.title("GUI test")
#defining the four sections of our stuff (year, title, author, etc
l1 = Label(window, text="Title",font="NSimSun 12 bold")
l1.grid(row=0,column=0)

l1 = Label(window, text="Author",font="NSimSun 12 bold")
l1.grid(row=0,column=2)

l1 = Label(window, text="Year",font="NSimSun 12 bold")
l1.grid(row=1,column=0)

l1 = Label(window, text="ISBN",font="NSimSun 12 bold")
l1.grid(row=1,column=2)

#DEFINING ENTRIES

titletext=StringVar()
e1=Entry(window,textvariable=titletext,font="NSimSun 12 bold",)
e1.grid(row=0,column=1)

authortext=StringVar()
e2=Entry(window,textvariable=authortext,font="NSimSun 12 bold")
e2.grid(row=0,column=3)

yeartext=StringVar()
e3=Entry(window,textvariable=yeartext,font="NSimSun 12 bold")
e3.grid(row=1,column=1)

ISBNtext=StringVar()
e4=Entry(window,textvariable=ISBNtext,font="NSimSun 12 bold")
e4.grid(row=1,column=3)

#listbox defining

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)


#scrollbar

sbl=Scrollbar(window)
sbl.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sbl.set)
sbl.configure(command=list1.yview)

b1=Button(window,text="View all",width=12,font="NSimSun 12 bold")
b1.grid(row=2,column=3)

b1=Button(window,text="Search",width=12,font="NSimSun 12 bold")
b1.grid(row=3,column=3)

b1=Button(window,text="Add Entry",width=12,font="NSimSun 12 bold")
b1.grid(row=4,column=3)

b1=Button(window,text="Renew Selected",width=12,font="NSimSun 12 bold")
b1.grid(row=5,column=3)

b1=Button(window,text="Delete All",width=12,font="NSimSun 12 bold")
b1.grid(row=6,column=3)

b1=Button(window,text="Close",width=12,font="NSimSun 12 bold")
b1.grid(row=7,column=3)

window.resizable(0,0)
window.configure(background="black")

window.mainloop()