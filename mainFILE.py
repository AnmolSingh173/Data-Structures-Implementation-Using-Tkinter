import tkinter as tk
m = tk.Tk()
m.geometry('500x600')
m.configure(bg='lightblue')

#WIDGETS WILL GO HERE
# w=tk.Button(m)
# w.pack()
heading=tk.Label(m,text="Visualization of Data Structures Using Tkinter",bg='lightBlue',fg='black',height=20,width=100)
heading.pack()
array = tk.Button(m,text="Use Arrays",width=50)
array.pack()
LL = tk.Button(m,text=" Linked List " , width= 50)
LL.pack()
DS3 =tk.Button(m,text=" Use Data Structure 3" , width=50)
DS3.pack()
DS4 =tk.Button(m,text=" Use Data Structure 4" , width=50)
DS4.pack()



exit = tk.Button(m,text="Exit GUI", width=25 , command=m.destroy)
exit.pack()
m.mainloop()