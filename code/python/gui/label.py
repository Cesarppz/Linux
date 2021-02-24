import tkinter

root = tkinter.Tk()
root.title('Hola')


miframe = tkinter.Frame(root,width=650,height=400)
miframe.pack()

Myimage = tkinter.PhotoImage(file='foto.png') #Colocar una imagen
milabel = tkinter.Label(miframe,image=Myimage)

#milabel = tkinter.Label(miframe,text='Hola internautas, corazones mios ...',font=(18),fg='red')
milabel.place(x=300,y=200) #Ubicar el texto 



root.mainloop()