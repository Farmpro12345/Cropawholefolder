import tkinter as tk
import main
window = tk.Tk()

greeting = tk.Label(text = "Welcome to picture cutter")
greeting.pack()


label = tk.Label(text="Input cordinates/dimensions under here!")
label.pack()

label = tk.Label(text="x1", width=50)
x1 = tk.Entry()
label.pack()
x1.pack()

label = tk.Label(text="y1")
y1 = tk.Entry()
label.pack()
y1.pack()

label = tk.Label(text="x2")
x2 = tk.Entry()
label.pack()
x2.pack()

label = tk.Label(text="y2")
y2 = tk.Entry()
label.pack()
y2.pack()

label = tk.Label(text="Input folder(use two slashes for windows)include extra slash on the end")
en2 = tk.Entry()
label.pack()
en2.pack()

label = tk.Label(text="Output folder(use two slashes for windows)include extra slash on the end")
en1 = tk.Entry()
label.pack()
en1.pack()

cord_input = ""
pic_input = ""
pic_output = ""
inx1 = 0
iny1 = 0
inx2 = 0
iny2 = 0

def submit():
    exec(open("main.py").read())
    global pic_input
    global pic_output
    global inx1
    global iny1
    global inx2
    global iny2
    global cord_input
    pic_output = en1.get()
    print(pic_output)
    pic_input = en2.get()
    print(pic_input)

    inx1 = int(x1.get())
    print(inx1)

    iny1 = int(y1.get())
    print(iny1)

    inx2 = int(x2.get())
    print(inx2)

    iny2 = int(y2.get())
    print(iny2)

    cord_input = (inx1,iny1,inx2,iny2)
    print(cord_input)

    #exec(open('main.py').read())


button = tk.Button(
    text="Crop!(run)",
    width=30,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda:[submit(), window.destroy()]

)

button.pack()
window.mainloop()

