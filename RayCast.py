from tkinter import *
import math

#vars

width , height = 500,500

Location =  [300,300]
PlayerAngle=90

ObjectWidth=100

Map = [
    [0,0,1,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,1],
    [1,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,1,0,0]
]

#constructors
root = Tk()
root.geometry(f'{width}x{height}+{ int(root.winfo_screenwidth() /2 - width / 2 )}+{ int(root.winfo_screenheight() /2 - height /2 )}')
root.overrideredirect(True)

#subs

def EXIT(event=None):
    root.destroy()
    sys.exit()

#mainloop

if __name__ == "__main__":
    print('[Run]Start here')

    Screen = Canvas(root, width=width+2 , height=height+2 , bg='gray60')
    Screen.place(x=-2,y=-2)

#binding
root.bind('<Escape>',EXIT)

mainloop()