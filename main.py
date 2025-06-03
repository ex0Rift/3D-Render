from tkinter import *
import sys

#vars

width , height = 500,500

facing = 'N'

GreenWalls = [
    [3,1]
]

Map = [
    [1,1,1,1,1,1,1,1],
    [1,0,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,0,1],
    [1,0,0,0,1,1,0,1],
    [1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,1],
    [1,2,1,0,1,1,0,1],
    [1,1,1,1,1,1,1,1]
]

#constructors

root = Tk()
root.geometry(f'{width}x{height}+{ int(root.winfo_screenwidth() /2 - width / 2 )}+{ int(root.winfo_screenheight() /2 - height /2 )}')
root.overrideredirect(True)

#subs

def ChangeSegmentState(Name):
    CurrentState = Screen.itemcget(Name,'state')
    if CurrentState == 'hidden':
        Screen.itemconfig(Name, state = 'normal')
    else:
        Screen.itemconfig(Name, state = 'hidden')

def EmptyScreen():
    for i in Screen.find_all():
        Screen.itemconfig(i,state='hidden')

def CheckForBlue(CHAU,CHAD):
    if Map[PlayerLocation[0]+CHAU][PlayerLocation[1]+CHAD] == 9:
        pass

def Keybinding(event):
    global facing , Map , PlayerLocation
    '''
    ############## the debug section ##############
    '''
    if event.keysym == '1':
        ChangeSegmentState(Mid)
    if event.keysym == '2':
        ChangeSegmentState(MLO)
    if event.keysym == '3':
        ChangeSegmentState(MRO)
    if event.keysym == '4':
        ChangeSegmentState(TO)
    if event.keysym == '5':
        ChangeSegmentState(BO)
    if event.keysym == '6':
        ChangeSegmentState(LTC)
    if event.keysym == '7':
        ChangeSegmentState(LBC)
    if event.keysym == '8':
        ChangeSegmentState(RTC)
    if event.keysym == '9':
        ChangeSegmentState(RBC)
    if event.keysym == '0':
        ChangeSegmentState(MLI)
    if event.keysym == 'q':
        ChangeSegmentState(MRI)
    if event.keysym == 'w':
        ChangeSegmentState(MIDI)
    if event.keysym == 'e':
        ChangeSegmentState(LO)
    if event.keysym == 't':
        ChangeSegmentState(RO)

    '''
    ############## The normal section ##############
    '''

    if event.keysym == 'Up':
        if facing=='N':
            if Map[PlayerLocation[0]-1][PlayerLocation[1]] != 1:       
                Map[PlayerLocation[0]][PlayerLocation[1]] = 0
                Map[PlayerLocation[0]-1][PlayerLocation[1]] = 2
                PlayerLocation = [PlayerLocation[0]-1,PlayerLocation[1]]

        if facing=='S':
            if Map[PlayerLocation[0]+1][PlayerLocation[1]] != 1:       
                Map[PlayerLocation[0]][PlayerLocation[1]] = 0
                Map[PlayerLocation[0]+1][PlayerLocation[1]] = 2
                PlayerLocation = [PlayerLocation[0]+1,PlayerLocation[1]]

        if facing == 'W':
            if Map[PlayerLocation[0]][PlayerLocation[1]-1] != 1:
                Map[PlayerLocation[0]][PlayerLocation[1]] = 0
                Map[PlayerLocation[0]][PlayerLocation[1]-1] = 2
                PlayerLocation = [PlayerLocation[0],PlayerLocation[1]-1]

        if facing == 'E':
            if Map[PlayerLocation[0]][PlayerLocation[1]+1] != 1:
                Map[PlayerLocation[0]][PlayerLocation[1]] = 0
                Map[PlayerLocation[0]][PlayerLocation[1]+1] = 2
                PlayerLocation = [PlayerLocation[0],PlayerLocation[1]+1]

    elif event.keysym == 'Left':
        if facing == 'N':
            facing = 'W'
        elif facing == 'E':
            facing = 'N'
        elif facing == 'S':
            facing = 'E'
        elif facing == 'W':
            facing = 'S'

    elif event.keysym == 'Right':
        if facing == 'N':
            facing = 'E'
        elif facing == 'E':
            facing = 'S'
        elif facing == 'S':
            facing = 'W'
        elif facing == 'W':
            facing = 'N'

    RefreshScreen()


def RefreshScreen():
    EmptyScreen()
    if facing == 'N':
        if Map[PlayerLocation[0]][PlayerLocation[1]-1]==1:
            ChangeSegmentState(LO)
        if Map[PlayerLocation[0]][PlayerLocation[1]+1]==1:
            ChangeSegmentState(RO)
        if Map[PlayerLocation[0]-1][PlayerLocation[1]-1]==1:
            ChangeSegmentState(MLI)
            if Map[PlayerLocation[0]][PlayerLocation[1]-1]==0:
                ChangeSegmentState(MLO)
        if Map[PlayerLocation[0]-1][PlayerLocation[1]+1]==1:
            ChangeSegmentState(MRI)
            if Map[PlayerLocation[0]][PlayerLocation[1]+1]==0:
                ChangeSegmentState(MRO)
        try:
            if Map[PlayerLocation[0]-2][PlayerLocation[1]]==1:
                ChangeSegmentState(MIDI)
        except:
            pass
        if Map[PlayerLocation[0]-1][PlayerLocation[1]]==1:
            ChangeSegmentState(Mid)
            Screen.itemconfig(MLI,state='hidden')
            Screen.itemconfig(MRI,state='hidden')
            Screen.itemconfig(MIDI,state='hidden')

    if facing == "W":
        if Map[PlayerLocation[0]+1][PlayerLocation[1]]==1:
            ChangeSegmentState(LO)
        if Map[PlayerLocation[0]-1][PlayerLocation[1]]==1:
            ChangeSegmentState(RO)
        if Map[PlayerLocation[0]+1][PlayerLocation[1]-1]==1:
            ChangeSegmentState(MLI)
            if Map[PlayerLocation[0]+1][PlayerLocation[1]]==0:
                ChangeSegmentState(MLO)
        if Map[PlayerLocation[0]-1][PlayerLocation[1]-1]==1:
            ChangeSegmentState(MRI)
            if Map[PlayerLocation[0]-1][PlayerLocation[1]]==0:
                ChangeSegmentState(MRO)
        try:
            if Map[PlayerLocation[0]][PlayerLocation[1]-2]==1:
                ChangeSegmentState(MIDI)
        except:
            pass
        if Map[PlayerLocation[0]][PlayerLocation[1]-1]==1:
            ChangeSegmentState(Mid)
            Screen.itemconfig(MLI,state='hidden')
            Screen.itemconfig(MRI,state='hidden')
            Screen.itemconfig(MIDI,state='hidden')

    if facing == "E":
        if Map[PlayerLocation[0]-1][PlayerLocation[1]]==1:
            ChangeSegmentState(LO)
        if Map[PlayerLocation[0]+1][PlayerLocation[1]]==1:
            ChangeSegmentState(RO)
        if Map[PlayerLocation[0]-1][PlayerLocation[1]+1]==1:
            ChangeSegmentState(MLI)
            if Map[PlayerLocation[0]-1][PlayerLocation[1]]==0:
                ChangeSegmentState(MLO) 
        if Map[PlayerLocation[0]+1][PlayerLocation[1]+1]==1:
            ChangeSegmentState(MRI)
            if Map[PlayerLocation[0]+1][PlayerLocation[1]]==0:
                ChangeSegmentState(MRO) 
        try:
            if Map[PlayerLocation[0]][PlayerLocation[1]+2]==1:
                ChangeSegmentState(MIDI)
        except:
            pass
        if Map[PlayerLocation[0]][PlayerLocation[1]+1]==1:
            ChangeSegmentState(Mid)
            Screen.itemconfig(MLI,state='hidden')
            Screen.itemconfig(MRI,state='hidden')
            Screen.itemconfig(MIDI,state='hidden')

    if facing == 'S':
        if Map[PlayerLocation[0]][PlayerLocation[1]+1]==1:
            ChangeSegmentState(LO)
        if Map[PlayerLocation[0]][PlayerLocation[1]-1]==1:
            ChangeSegmentState(RO)
        if Map[PlayerLocation[0]+1][PlayerLocation[1]+1]==1:
            ChangeSegmentState(MLI)
            if Map[PlayerLocation[0]][PlayerLocation[1]+1]==0:
                ChangeSegmentState(MLO)
        if Map[PlayerLocation[0]+1][PlayerLocation[1]-1]==1:
            ChangeSegmentState(MRI)
            if Map[PlayerLocation[0]][PlayerLocation[1]-1]==0:
                ChangeSegmentState(MRO)
        try:
            if Map[PlayerLocation[0]+2][PlayerLocation[1]]==1:
                ChangeSegmentState(MIDI)
        except:
            pass
        if Map[PlayerLocation[0]+1][PlayerLocation[1]]==1:
            ChangeSegmentState(Mid)
            Screen.itemconfig(MLI,state='hidden')
            Screen.itemconfig(MRI,state='hidden')
            Screen.itemconfig(MIDI,state='hidden')
        




def EXIT(event=None):
    root.destroy()
    sys.exit()

#mainloop and start

if __name__ == "__main__":
    print('[Run]Start here')

    Screen = Canvas(root, width=width+2 , height=height+2 , bg='gray60')
    Screen.place(x=-2,y=-2)

    '''
    ############## Create screen Segments ##############
    '''
    Mid=Screen.create_rectangle(100,100,400,400,fill='gray60',outline='gold',width=5,state='hidden')
    MIDI=Screen.create_rectangle(200,200,300,300,fill='gray60',outline='gold',width=5,state='hidden')

    TO=Screen.create_polygon(0,0,100,100,400,100,500,0,fill='gray60',outline='gold',width=5,state='hidden')
    BO=Screen.create_polygon(0,500,100,400,400,400,500,500,fill='gray60',outline='gold',width=5,state='hidden')

    LO=Screen.create_polygon(0,0,100,100,100,400,0,500,fill='gray60',outline='gold',width=5,state='hidden')
    RO=Screen.create_polygon(500,0,400,100,400,400,500,500,fill='gray60',outline='gold',width=5,state='hidden')

    MLO=Screen.create_rectangle(0,100,100,400,fill='gray60',outline='gold',width=5,state='hidden')
    MRO=Screen.create_rectangle(400,100,500,400,fill='gray60',outline='gold',width=5,state='hidden')

    MLI=Screen.create_polygon(100,100,200,200,200,300,100,400,fill='gray60',outline='gold',width=5,state='hidden')
    MRI=Screen.create_polygon(400,100,300,200,300,300,400,400,fill='gray60',outline='gold',width=5,state='hidden')

    LTC=Screen.create_polygon(0,0,100,100,0,100,fill='gray60',outline='gold',width=5,state='hidden')
    LBC=Screen.create_polygon(0,500,100,400,0,400,fill='gray60',outline='gold',width=5,state='hidden')

    RTC=Screen.create_polygon(500,0,400,100,500,100,fill='gray60',outline='gold',width=5,state='hidden')
    RBC=Screen.create_polygon(500,500,400,400,500,400,fill='gray60',outline='gold',width=5,state='hidden')

    '''
    ############## Load Map ##############
    '''
    for i in range(len(Map)-1):
        for j in range(len(Map[i])-1):
            if Map[i][j]==2:
                PlayerLocation=[i,j]
    try:
        print(PlayerLocation)
    except:
        print('[FATAL EEROR]PLAYER NOT ON MAP CLOSING')
        EXIT()

    if Map[PlayerLocation[0]][PlayerLocation[1]-1]==1:
        ChangeSegmentState(LO)
    if Map[PlayerLocation[0]][PlayerLocation[1]+1]==1:
        ChangeSegmentState(RO)
    if Map[PlayerLocation[0]-1][PlayerLocation[1]-1]==1:
        ChangeSegmentState(MLI)
        if Map[PlayerLocation[0]][PlayerLocation[1]-1]==0:
            ChangeSegmentState(MLO)
    if Map[PlayerLocation[0]-1][PlayerLocation[1]+1]==1:
        ChangeSegmentState(MRI)
        if Map[PlayerLocation[0]][PlayerLocation[1]+1]==0:
            ChangeSegmentState(MRO)
    if Map[PlayerLocation[0]-2][PlayerLocation[1]]==1:
        ChangeSegmentState(MIDI)
    if Map[PlayerLocation[0]-1][PlayerLocation[1]]==1:
            ChangeSegmentState(Mid)
            Screen.itemconfig(MLI,state='hidden')
            Screen.itemconfig(MRI,state='hidden')

#binding
root.bind('<Escape>',EXIT)
root.bind('<Key>',Keybinding)

mainloop()