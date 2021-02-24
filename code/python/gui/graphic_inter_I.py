import tkinter

raiz = tkinter.Tk()

raiz.title('Hola mundo')
#raiz.resizable(True,1)
raiz.geometry('650x300')
raiz.config(bg='green')

myframe = tkinter.Frame()  #Craer un frame
myframe.pack(side='bottom')
myframe.config(width='650',height='350',bg='blue')

tkinter.mainloop()
