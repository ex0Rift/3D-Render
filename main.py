from tkinter import *
import sys

#vars

width , height = 500,500

facing = 'N'

MiniMapObjects=[]

Map=[]

with open('Map.txt','r')as file:
    while True:
        Temp=file.readline().strip()
        if Temp == '':
            break

        Temp=Temp.split(' ')
        for i in range(len(Temp)):
            Temp[i]=int(Temp[i])


        Map.append(Temp)


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
            MiniMap.itemconfig(NPointer,state='hidden')
            MiniMap.itemconfig(WPointer,state='normal')
        elif facing == 'E':
            facing = 'N'
            MiniMap.itemconfig(EPointer,state='hidden')
            MiniMap.itemconfig(NPointer,state='normal')
        elif facing == 'S':
            facing = 'E'
            MiniMap.itemconfig(SPointer,state='hidden')
            MiniMap.itemconfig(EPointer,state='normal')
        elif facing == 'W':
            facing = 'S'
            MiniMap.itemconfig(WPointer,state='hidden')
            MiniMap.itemconfig(SPointer,state='normal')

    elif event.keysym == 'Right':
        if facing == 'N':
            facing = 'E'
            MiniMap.itemconfig(NPointer,state='hidden')
            MiniMap.itemconfig(EPointer,state='normal')
        elif facing == 'E':
            facing = 'S'
            MiniMap.itemconfig(EPointer,state='hidden')
            MiniMap.itemconfig(SPointer,state='normal')
        elif facing == 'S':
            facing = 'W'
            MiniMap.itemconfig(SPointer,state='hidden')
            MiniMap.itemconfig(WPointer,state='normal')
        elif facing == 'W':
            facing = 'N'
            MiniMap.itemconfig(WPointer,state='hidden')
            MiniMap.itemconfig(NPointer,state='normal')

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
                if Map[PlayerLocation[0]-1][PlayerLocation[1]-1]==0:
                    ChangeSegmentState(LMI)
                if Map[PlayerLocation[0]-1][PlayerLocation[1]+1]==0:
                    ChangeSegmentState(RMI)
        except:
            pass
        if Map[PlayerLocation[0]-1][PlayerLocation[1]]==1:
            ChangeSegmentState(Mid)
            Screen.itemconfig(MLI,state='hidden')
            Screen.itemconfig(MRI,state='hidden')
            Screen.itemconfig(MIDI,state='hidden')
            Screen.itemconfig(RMI,state='hidden')
            Screen.itemconfig(LMI,state='hidden')

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
                if Map[PlayerLocation[0]+1][PlayerLocation[1]-1]==0:
                    ChangeSegmentState(LMI)
                if Map[PlayerLocation[0]-1][PlayerLocation[1]-1]==0:
                    ChangeSegmentState(RMI)
        except:
            pass
        if Map[PlayerLocation[0]][PlayerLocation[1]-1]==1:
            ChangeSegmentState(Mid)
            Screen.itemconfig(MLI,state='hidden')
            Screen.itemconfig(MRI,state='hidden')
            Screen.itemconfig(MIDI,state='hidden')
            Screen.itemconfig(RMI,state='hidden')
            Screen.itemconfig(LMI,state='hidden')

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
                if Map[PlayerLocation[0]-1][PlayerLocation[1]+1]==0:
                    ChangeSegmentState(LMI)
                if Map[PlayerLocation[0]+1][PlayerLocation[1]+1]==0:
                    ChangeSegmentState(RMI)
        except:
            pass
        if Map[PlayerLocation[0]][PlayerLocation[1]+1]==1:
            ChangeSegmentState(Mid)
            Screen.itemconfig(MLI,state='hidden')
            Screen.itemconfig(MRI,state='hidden')
            Screen.itemconfig(MIDI,state='hidden')
            Screen.itemconfig(RMI,state='hidden')
            Screen.itemconfig(LMI,state='hidden')

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
                if Map[PlayerLocation[0]+1][PlayerLocation[1]+1]==0:
                    ChangeSegmentState(LMI)
                if Map[PlayerLocation[0]+1][PlayerLocation[1]-1]==0:
                    ChangeSegmentState(RMI)
        except:
            pass
        if Map[PlayerLocation[0]+1][PlayerLocation[1]]==1:
            ChangeSegmentState(Mid)
            Screen.itemconfig(MLI,state='hidden')
            Screen.itemconfig(MRI,state='hidden')
            Screen.itemconfig(MIDI,state='hidden')
            Screen.itemconfig(RMI,state='hidden')
            Screen.itemconfig(LMI,state='hidden')
        
    '''
    ############## MiniMap code ##############
    '''
    if Map[PlayerLocation[0]][PlayerLocation[1]-1]==1:
        MiniMap.itemconfig(MiniMapObjects[11],state='normal')
    else:
        MiniMap.itemconfig(MiniMapObjects[11],state='hidden')
    if Map[PlayerLocation[0]][PlayerLocation[1]+1]==1:
        MiniMap.itemconfig(MiniMapObjects[13],state='normal')
    else:
        MiniMap.itemconfig(MiniMapObjects[13],state='hidden')
    if Map[PlayerLocation[0]-1][PlayerLocation[1]]==1:
        MiniMap.itemconfig(MiniMapObjects[7],state='normal')
    else:
        MiniMap.itemconfig(MiniMapObjects[7],state='hidden')
    if Map[PlayerLocation[0]+1][PlayerLocation[1]]==1:
        MiniMap.itemconfig(MiniMapObjects[17],state='normal')
    else:
        MiniMap.itemconfig(MiniMapObjects[17],state='hidden')
    if Map[PlayerLocation[0]-1][PlayerLocation[1]-1]==1:
        MiniMap.itemconfig(MiniMapObjects[6],state='normal')
    else:
        MiniMap.itemconfig(MiniMapObjects[6],state='hidden')
    if Map[PlayerLocation[0]-1][PlayerLocation[1]+1]==1:
        MiniMap.itemconfig(MiniMapObjects[8],state='normal')
    else:
        MiniMap.itemconfig(MiniMapObjects[8],state='hidden')
    if Map[PlayerLocation[0]+1][PlayerLocation[1]-1]==1:
        MiniMap.itemconfig(MiniMapObjects[16],state='normal')
    else:
        MiniMap.itemconfig(MiniMapObjects[16],state='hidden')
    if Map[PlayerLocation[0]+1][PlayerLocation[1]+1]==1:
        MiniMap.itemconfig(MiniMapObjects[18],state='normal')
    else:
        MiniMap.itemconfig(MiniMapObjects[18],state='hidden')
    try:
        if Map[PlayerLocation[0]-2][PlayerLocation[1]-2]==1:
            MiniMap.itemconfig(MiniMapObjects[0],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[0],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]-2][PlayerLocation[1]-1]==1:
            MiniMap.itemconfig(MiniMapObjects[1],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[1],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]-2][PlayerLocation[1]]==1:
            MiniMap.itemconfig(MiniMapObjects[2],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[2],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]-2][PlayerLocation[1]+1]==1:
            MiniMap.itemconfig(MiniMapObjects[3],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[3],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]-2][PlayerLocation[1]+2]==1:
            MiniMap.itemconfig(MiniMapObjects[4],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[4],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]+2][PlayerLocation[1]-2]==1:
            MiniMap.itemconfig(MiniMapObjects[20],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[20],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]+2][PlayerLocation[1]-1]==1:
            MiniMap.itemconfig(MiniMapObjects[21],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[21],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]+2][PlayerLocation[1]]==1:
            MiniMap.itemconfig(MiniMapObjects[22],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[22],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]+2][PlayerLocation[1]+1]==1:
            MiniMap.itemconfig(MiniMapObjects[23],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[23],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]+2][PlayerLocation[1]+2]==1:
            MiniMap.itemconfig(MiniMapObjects[24],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[24],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]-1][PlayerLocation[1]-2]==1:
            MiniMap.itemconfig(MiniMapObjects[5],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[5],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]][PlayerLocation[1]-2]==1:
            MiniMap.itemconfig(MiniMapObjects[10],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[10],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]+1][PlayerLocation[1]-2]==1:
            MiniMap.itemconfig(MiniMapObjects[15],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[15],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]-1][PlayerLocation[1]+2]==1:
            MiniMap.itemconfig(MiniMapObjects[9],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[9],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]][PlayerLocation[1]+2]==1:
            MiniMap.itemconfig(MiniMapObjects[14],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[14],state='hidden')
    except:
        pass
    try:
        if Map[PlayerLocation[0]+1][PlayerLocation[1]+2]==1:
            MiniMap.itemconfig(MiniMapObjects[19],state='normal')
        else:
            MiniMap.itemconfig(MiniMapObjects[19],state='hidden')
    except:
        pass

    '''
    ############## Win Logic ##############
    '''
    if PlayerLocation[0]==WinLocation[0] and PlayerLocation[1]==WinLocation[1]:
        print('WIN')
        root.destroy()

        Win = Tk()

        Win.config(bg='green')
        
        Win.attributes('-fullscreen',True)

        Win.mainloop()

        
def EXIT(event=None):
    root.destroy()
    sys.exit()

#mainloop and start

if __name__ == "__main__":
    print('[Run]Start here')

    Screen = Canvas(root, width=width+2 , height=height+2 , bg='gray60')
    Screen.place(x=-2,y=-2)

    MiniMap = Canvas(root,width=100,height=100,bg='gray60')
    MiniMap.place(x=10,y=10)

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

    LMI=Screen.create_rectangle(100,200,200,300,fill='gray60',outline='gold',width=5,state='hidden')
    RMI=Screen.create_rectangle(300,200,400,300,fill='gray60',outline='gold',width=5,state='hidden')

    '''
    ############## Create Map segments ##############
    '''

    C=[0,0,20,20]
    for i in range(5):
        for j in range(5):
            MiniMapObjects.append(MiniMap.create_rectangle(C[0],C[1],C[2],C[3],fill='gold',state='hidden'))
            C[0]+=20
            C[2]+=20
        C[0]=0
        C[2]=20
        C[1]+=20
        C[3]+=20

    MiniMap.itemconfig(MiniMapObjects[12],fill='red',state='normal')

    NPointer = MiniMap.create_polygon(40,60,60,60,50,40,fill='darkred')
    SPointer = MiniMap.create_polygon(40,40,60,40,50,60,fill='darkred',state='hidden')
    EPointer = MiniMap.create_polygon(40,40,40,60,60,50,fill='darkred',state='hidden')
    WPointer = MiniMap.create_polygon(60,40,60,60,40,50,fill='darkred',state='hidden')

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

    for i in range(len(Map)-1):
        for j in range(len(Map[i])-1):
            if Map[i][j]==3:
                WinLocation=[i,j]
    try:
        print(WinLocation)
    except:
        print('[FATAL EEROR]NO WIN LOCATION')
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

    MiniMap.place_forget()


#binding
root.bind('<Escape>',EXIT)
root.bind('<Key>',Keybinding)



mainloop()