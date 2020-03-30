from tkinter import *

root = Tk()

aframe = Frame(root, height=800, width=800)
aframe.pack()

headLabel = Label(aframe, text="FOSS Lab Micro Project\n\n", bg="black", fg="white", width=800)
headLabel.pack(fill=X)

h1Label = Label(aframe, text="Group Members\n", bg="black", fg="white")
h1Label.pack(fill=X)

nLabel = Label(aframe, text="1. Christy Thomas\n2. Deepu Cyriac\n3. Devana C U\n4. Devanandan S\n", bg="black", fg="white")
nLabel.pack(fill=X)

bframe = Frame(root, height=800, width=800)
bframe.pack(side=BOTTOM)


def syscmd():
    import subprocess

    out = subprocess.Popen(['cat','/proc/uptime'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    stdout,stderr = out.communicate()

    b = "Running time \n"
    i = "Idle time \n"

    textbox1.insert(INSERT, "\n"+b)
    textbox2.insert(INSERT, "\n"+i)

    textbox1.insert(INSERT, str(stdout.split()[0])+"\n")
    textbox2.insert(INSERT, str(stdout.split()[1])+"\n")


btlabel = Label(bframe, text="Click the button to view the running time and idle time", fg="black", width=800)
button1 = Button(bframe, text="Execute Command", command=syscmd)

btlabel.pack()
button1.pack()


textbox1 = Text(root)
textbox2 = Text(root)

textbox1.pack()
textbox2.pack()

root.mainloop()