from Tkinter import*
import random
window2 = Tk()

pc = random.randint(1,3)

b = IntVar()
b.set(0)
t = [ 
 ("rock",1),
 ("paper",2),
 ("scissors",3),
]
def sc():
    if b.get()==1 and b.get()== pc:
        Label(window2,text="tie").pack()
        
    elif b.get()==1:
        if pc == 2:
         Label(window2,text="you loose to paper").pack()
        else:
          Label(window2,text="you win to scissors").pack()

         
    if b.get()==2 and b.get()== pc:
        Label(window2,text="tie").pack()
        
    elif b.get()==2:
       if pc == 3:
         Label(window2,text="you loose scissors").pack()
       else:
          Label(window2,text="you win to rock").pack()

    if b.get()==3 and b.get()== pc:
        Label(window2,text="tie").pack()
        
    elif b.get()==3:
       if pc == 1:
         Label(window2,text="you loose to rock").pack()
       else:
         Label(window2,text="you win to paper").pack()

        
e = Label(window2,text="rock, paper, scissors?",
justify = LEFT,
padx = 20).pack()
for txt, val in t:
    Radiobutton(window2,
     text = txt,
     indicatoron = 0,
     width = 20,
     padx = 20,
     variable=b,
     command= sc,
     value=val).pack(anchor=W)
but = Button(window2,text="Quit",command=window2.destroy,
padx = 14).pack()
mainloop()        





