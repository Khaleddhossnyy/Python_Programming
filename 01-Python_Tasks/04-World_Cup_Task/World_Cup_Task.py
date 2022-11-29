from tkinter import * 
#---------------------------------------
def SEN_GOAL():
	global SEN_GOAL_VALUE
	SEN_GOAL_VALUE=SEN_GOAL_VALUE+1
	print(SEN_GOAL_VALUE)
	label_SEN_GOAL_Value= Label(Window_1, text=SEN_GOAL_VALUE , bd='12', bg='gold')
	canvas.create_window(60,30,window=label_SEN_GOAL_Value)
#---------------------------------------
def SEN_GOAL_Canceled():
	global SEN_GOAL_VALUE
	if SEN_GOAL_VALUE:
		SEN_GOAL_VALUE=SEN_GOAL_VALUE-1
		print(SEN_GOAL_VALUE)
		label_SEN_GOAL_Canceled= Label(Window_1, text=SEN_GOAL_VALUE , bd='12', bg='gold')
		canvas.create_window(60,30,window=label_SEN_GOAL_Canceled)
#---------------------------------------
def HOL_GOAL():
	global HOL_GOAL_VALUE
	HOL_GOAL_VALUE=HOL_GOAL_VALUE+1
	print(HOL_GOAL_VALUE)
	label_HOL_GOAL_Value= Label(Window_1, text=HOL_GOAL_VALUE , bd='12', bg='royal blue')
	canvas.create_window(155,30,window=label_HOL_GOAL_Value)
#---------------------------------------
def HOL_GOAL_Canceled():
	global HOL_GOAL_VALUE
	if  HOL_GOAL_VALUE != 0:
		HOL_GOAL_VALUE=HOL_GOAL_VALUE-1
		print(HOL_GOAL_VALUE)
		label_HOL_GOAL_Value_Canceled= Label(Window_1, text=HOL_GOAL_VALUE , bd='12', bg='royal blue')
		canvas.create_window(155,30,window=label_HOL_GOAL_Value_Canceled)
#---------------------------------------
def END_OF_Time():
	if HOL_GOAL_VALUE < SEN_GOAL_VALUE:
		label_SEN_Wins = Label(Window_1, text="Senegal is the winner" , bd='12', bg='gold')
		canvas_Winner.create_window(105,30,window=label_SEN_Wins)
	elif HOL_GOAL_VALUE > SEN_GOAL_VALUE:
		label_HOL_Wins = Label(Window_1, text="Holland is the winner" , bd='12', bg='royal Blue')
		canvas_Winner.create_window(105,30,window=label_HOL_Wins)
	elif HOL_GOAL_VALUE == SEN_GOAL_VALUE:
		label_Draw = Label(Window_1, text="Match ended with a draw" , bd='12', bg='light cyan')
		canvas_Winner.create_window(105,30,window=label_Draw)
#---------------------------------------
Window_1=Tk();
Window_1.title("World Cup Task") #title of the window
Window_1.geometry('400x400') #set the width and height of the window
Window_1.configure(bg='floral white')
#--------------------------------------------------------------------------
photo_SEN = PhotoImage(file='Senegal.png')
photo_SEN = photo_SEN.subsample(8,8) #columns,rows 
label_SEN = Label(Window_1, image = photo_SEN)
label_SEN.place(x=5,y=20)
#--------------------------------------------------------------------------
SEN_GOAL_VALUE=0
Button_SEN_GOAL =Button(Window_1, text="SEN GOAL", bd = '10', bg ='gold',command = SEN_GOAL) #create a button with a command given to it every time this button is pressed
Button_SEN_GOAL.place(x=45,y=150)
#--------------------------------------------------------------------------
photo_HOL = PhotoImage(file='Holand.png')
photo_HOL = photo_HOL.subsample(8,8) #columns,rows 
label_HOL = Label(Window_1, image = photo_HOL)
label_HOL.place(x=230,y=20)
#--------------------------------------------------------------------------
HOL_GOAL_VALUE=0
Button_HOL_GOAL =Button(Window_1, text="HOL GOAL", bd = '10', bg ='royal blue',command =HOL_GOAL) #create a button with a command given to it every time this button is pressed
Button_HOL_GOAL.place(x=270,y=150)
#--------------------------------------------------------------------------
#photo_REC = PhotoImage(file='rectangle.png')
#photo_REC = photo_REC.subsample(2,2) #columns,rows 
#label_REC = Label(Window_1, image = photo_REC, bg='floral white')
#label_REC.place(x=70,y=220)
canvas = Canvas(Window_1,height=60,width=212)
canvas.place(x=90,y=220)

canvas.create_rectangle(2,2,212,60,outline="black",fill="floral white")

label_SEN_GOAL_Value= Label(Window_1, text=SEN_GOAL_VALUE , bd='12', bg='gold')
canvas.create_window(60,30,window=label_SEN_GOAL_Value)

label_HOL_GOAL_Value= Label(Window_1, text=HOL_GOAL_VALUE , bd='12', bg='royal blue')
canvas.create_window(155,30,window=label_HOL_GOAL_Value)
#--------------------------------------------------------------------------
canvas_Winner= Canvas(Window_1,height=60,width=212)
canvas_Winner.place(x=90,y=300)

canvas_Winner.create_rectangle(2,2,212,60,outline="black",fill="floral white")
#--------------------------------------------------------------------------
Button_END_Time =Button(Window_1, text="Time Ended", bd = '10', bg ='light cyan',command =END_OF_Time)
Button_END_Time.place(x=155,y=150)
#--------------------------------------------------------------------------
Button_des = Button(Window_1, text="Exit App", bd='5' ,bg = 'light cyan',command = Window_1.destroy)
Button_des.place(x=320,y=360)
#--------------------------------------------------------------------------
Button_SEN_GOAL_Canceled = Button(Window_1, text="Cancel GOAL", bd = '1', bg ='gold',command =  SEN_GOAL_Canceled)
Button_SEN_GOAL_Canceled.place(x=5,y=230)
#--------------------------------------------------------------------------
Button_HOL_GOAL_Canceled = Button(Window_1, text="Cancel GOAL", bd = '1', bg ='royal blue',command =  HOL_GOAL_Canceled)
Button_HOL_GOAL_Canceled.place(x=310,y=230)
#--------------------------------------------------------------------------

Window_1.mainloop()