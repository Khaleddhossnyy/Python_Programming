import pygame #pyhton module i will be using in all phases of my snake game 
import time
import random #will be used to generate random co-ordinates for the snake food
from tkinter import *
#------------------------------------------------------
#Game_Over_Flag = 0 #flag to indicate the ending of the game and initialize it with zero 
#Close_The_Game_Flag = 0 #flag to indicate if the user wants to close the game 
#------------------------------------------------------
#defining functions to be used by tkinter 
#------------------------------------------------------
def Snake_Color_Choosed(color):
	global Snake_Color
	Snake_Color = color

def Game_Difficulty_Choosed(diff):
	global Snake_Speed
	Snake_Speed = diff

def Game_Start():
	global Game_Start_Flag 
	Game_Start_Flag=1
	Window_1.destroy()
#------------------------------------------------------
#Defining some colors to be used along the project
#------------------------------------------------------
WHITE =      (255,255,255)
BLUE  =      (0,0,255)
GREEN =      (0,255,0)
RED   =      (255,0,0)
GRAY  =      (127,127,127) 
CYAN  =      (0,255,255)
BLACK =      (0,0,0)
#------------------------------------------------------
#Defining some global variables 
#------------------------------------------------------
Snake_Color = RED #to be set using tkinter , deafult color
Snake_Size =12
Snake_Speed=25 #(50-30) #to be set based on the level choosing usng tkinter , default difficulty
X_Position=0
Y_Position=0
#-----------------------------------------------------
Game_Start_Flag=0;
#------------------------------------------------------
#functions to be used 
#------------------------------------------------------
def Set_Snake_Color(Color):
	global Snake_Color
	Snake_Color = Color

def Set_Snake_Speed(Speed):
	global Snake_Speed
	Snake_Speed = Speed

def Draw_Snake():
	pygame.draw.circle(Game_Screen,Snake_Color,[X_CoOrdinate_Start,Y_CoOrdinate_Start],Snake_Size) #screen,color,position,radius
	
def CoOrdinates_Change(event_to_check_for):
	if event_to_check_for.key == pygame.K_LEFT: #left arrow is pressed
		X_CoOrdinate_Change = -5
		Y_CoOrdinate_Change = 0
	elif event_to_check_for.key == pygame.K_RIGHT: #right arrow is pressed
		X_CoOrdinate_Change = 5
		Y_CoOrdinate_Change = 0
	elif event_to_check_for.key == pygame.K_UP: #up arrow is pressed
		X_CoOrdinate_Change = 0
		Y_CoOrdinate_Change = -5
	elif event_to_check_for.key == pygame.K_DOWN: #down arrow is pressed
		X_CoOrdinate_Change = 0
		Y_CoOrdinate_Change = 5

def Set_Message_X_Y_Position(x,y):
	global X_Position
	global Y_Position
	X_Position=x
	Y_Position=y
		
def Move_Snake():
	X_CoOrdinate_Start = X_CoOrdinate_Start + X_CoOrdinate_Change  
	Y_CoOrdinate_Start = Y_CoOrdinate_Start + Y_CoOrdinate_Change

def Write_message(Message_to_Write,Color_of_The_Message):
	font_style =pygame.font.SysFont(None,42)
	Message_to_Write = font_style.render(Message_to_Write,True,Color_of_The_Message)
	Game_Screen.blit(Message_to_Write,[X_Position,Y_Position])

def Boundaries_Check():
	global Game_Over_Flag
	global Close_The_Game_Flag
	if X_CoOrdinate_Start >= 799 or X_CoOrdinate_Start <0 or Y_CoOrdinate_Start >= 799 or Y_CoOrdinate_Start <0:
		Close_The_Game_Flag=1
		

def Draw_Snake_From_Snake_Array(Snake_Size,Snake_Array): #after eating food the snake length will increase so we will need to draw the new snake which 
	for Each_Part in Snake_Array:
		pygame.draw.rect(Game_Screen,Snake_Color,[Each_Part[0],Each_Part[1],Snake_Size,Snake_Size]) #screen,color,position,radius

def Generate_Food():
	global Snake_Food_x
	global Snake_Food_y
	Snake_Food_x = round(random.randrange(0,600-8)/10.0 *10.0) #equation to generate random x-co-ordinate
	Snake_Food_y = round(random.randrange(0,500-8)/10.0 *10.0) #equation to generate random x-co-ordinate
	pygame.draw.rect(Game_Screen,Snake_Color,[Snake_Food_x,Snake_Food_y,7,7]) #draw the food on the screen 

def Snake_Array_Append_Entry():
	global Snake_Array
	global Snake_Array_Entry
	Snake_Array_Entry.append(X_CoOrdinate_Start)
	Snake_Array_Entry.append(Y_CoOrdinate_Start)
	Snake_Array.append(Snake_Array_Entry)
	
def Snake_Array_Modfication(): #will change the size of the snake array if it exceeded the length of the snake after eating food  
	global Snake_Array
	if len(Snake_Array) > Snake_Length:
		del Snake_Array[0] #delete

def Close_PlayAgain_The_Game():
	global Close_The_Game_Flag
	global Game_Over_Flag
	while Close_The_Game_Flag == 0: #flag is up 
		Game_Screen.fill(BLACK)
		Set_Message_X_Y_Position(100,340)
		Write_message("!! YOU LOST, GAME OVER",WHITE)
		Set_Message_X_Y_Position(100,440)
		Write_message("!! To Play again , Press --> A",RED)
		Set_Message_X_Y_Position(100,540)
		Write_message("!! To QUIT , Press --> Q",RED)
		pygame.display.update()
		Event = pygame.event.get()
		for eventt in Event :
			if eventt.type == pygame.KEYDOWN:
				if eventt.key == pygame.K_q:
					Game_Over_Flag =1
					Close_The_Game_Flag = 1 #to break the loop and go to the end game loop
				if eventt.key == pygame.K_a:
					#print("here")
					Game_Over_Flag =0
					#Close_The_Game_Flag = 0
					Play_The_Game()

def Play_The_Game():
	#global Game_Over_Flag
	#global Close_The_Game_Flag
	Game_Over_Flag = 0 #flag to indicate the ending of the game and initialize it with zero 
	Close_The_Game_Flag = 0
	X_CoOrdinate_Start=400
	Y_CoOrdinate_Start=350
	X_CoOrdinate_Change = 0 #to hold the change that will happen in the x co ordinates when moving the snake
	Y_CoOrdinate_Change = 0 #to hold the change that will happen in the y co ordinates when moving the snake
	Snake_Array = []  #array which will hold the length of the snake ,each element here will be a list itslef to hold x-co-ordinate and y-cordinate ex=[[0,0],[2,2]] 
	Snake_Length = 1 #initialize the length of the snake with 1
	Snake_Food_x=round(random.randrange(0,800-10)/10.0) *10.0
	Snake_Food_y=round(random.randrange(0,700-10)/10.0) *10.0
	Help_Flag=0
	
	while Game_Over_Flag == 0: #keep the game running until the user loses 
		#pygame.display.update()
		#Close_The_Game()
		#Close_PlayAgain_The_Game()
		while Close_The_Game_Flag == 1: #close the game flag is up 
			Game_Screen.fill(BLACK)
			Set_Message_X_Y_Position(200,140)
			Write_message("!! YOU LOST, GAME OVER",WHITE)
			Set_Message_X_Y_Position(200,240)
			Write_message(" To Play again , Press --> A",RED)
			Set_Message_X_Y_Position(200,340)
			Write_message(" To QUIT , Press --> Q",RED)
			Set_Message_X_Y_Position(200,440)
			Write_message(" For HELP, Press --> H",RED)
			pygame.display.update()
			Event = pygame.event.get()
			for eventt in Event :
				if eventt.type == pygame.KEYDOWN:
					if eventt.key == pygame.K_q:
						Game_Over_Flag =1
						Close_The_Game_Flag = 0 #to break the loop and go to the end game loop
					if eventt.key == pygame.K_a:
						#print("here")
						#Game_Over_Flag =0
						#Close_The_Game_Flag = 0
						Play_The_Game()
					if eventt.key == pygame.K_h:
						while Help_Flag == 0:
							Game_Screen.fill(RED)						
							Set_Message_X_Y_Position(270,50)
							Write_message("--- HELP PAGE ---",BLACK)
							Set_Message_X_Y_Position(10,200)
							Write_message("Our game got 2 simple rules :",WHITE)
							Set_Message_X_Y_Position(10,300)
							Write_message("1) First rule : you can't touch any of the four borders",WHITE)
							Set_Message_X_Y_Position(10,400)
							Write_message("2) Second rule : you can't eat yourself",WHITE)
							Set_Message_X_Y_Position(10,500)
							Write_message("3) Third rule : Press on your desired color and difficulty",WHITE)
							Set_Message_X_Y_Position(10,620)
							Write_message(" To Exit HELP page press --> C",WHITE)
							pygame.display.update()
							Eventtt = pygame.event.get()
							for eventtt in Eventtt:
								if eventtt.type == pygame.KEYDOWN :
									if eventtt.key == pygame.K_c:
										Help_Flag =1
		Ev = pygame.event.get()
		for event in Ev:
			#print(i) #print the event 
			if event.type == pygame.QUIT: #there is an event in pygame called QUIT which aim to close the screen if the Close button is pressed
				#print("Here")
				Game_Over_Flag = 1 #if game over flag is set then the user lost and the game should close
			if event.type == pygame.KEYDOWN: #indication that a key is pressed 
				#CoOrdinates_Change(event)
				if event.key == pygame.K_LEFT: #left arrow is pressed
					X_CoOrdinate_Change = -5
					Y_CoOrdinate_Change = 0
				elif event.key == pygame.K_RIGHT: #right arrow is pressed
					X_CoOrdinate_Change = 5
					Y_CoOrdinate_Change = 0
				elif event.key == pygame.K_UP: #up arrow is pressed
					X_CoOrdinate_Change = 0
					Y_CoOrdinate_Change = -5
				elif event.key == pygame.K_DOWN: #down arrow is pressed
					X_CoOrdinate_Change = 0
					Y_CoOrdinate_Change = 5
					
		if X_CoOrdinate_Start >= 800 or X_CoOrdinate_Start <0 or Y_CoOrdinate_Start >= 700 or Y_CoOrdinate_Start <0:
			Close_The_Game_Flag=1		
		#Boundaries_Check() #check if the snake reaches the boundaries then the game is over
		
		X_CoOrdinate_Start += X_CoOrdinate_Change 
		#print(X_CoOrdinate_Start)		
		Y_CoOrdinate_Start += Y_CoOrdinate_Change
		#print(Y_CoOrdinate_Start)
		
		Game_Screen.fill(CYAN) #new frame
		
		#Generate_Food() #generate the snake food in different locations
		pygame.draw.rect(Game_Screen,BLACK,[Snake_Food_x,Snake_Food_y,Snake_Size,Snake_Size]) #draw the food on the screen 
		
		Snake_Header = []
		Snake_Header.append(X_CoOrdinate_Start)
		Snake_Header.append(Y_CoOrdinate_Start)
		Snake_Array.append(Snake_Header)
		
		#Snake_Array_Append_Entry()
		
		#Snake_Array_Modfication() #to discretely before eating draw the snake not continously , draw it like this . not like this ....... 
		if len(Snake_Array) > Snake_Length:
			del Snake_Array[0] #delete
		
		#if the snake revolved around itself raise the flag of losing the game 
		for n in Snake_Array[:-1]:
			if n == Snake_Header:
				Close_The_Game_Flag = 1
		
		#Draw_Snake_From_Snake_Array()
		Draw_Snake_From_Snake_Array(Snake_Size,Snake_Array)
		#for i in Snake_Array:
			#pygame.draw.circle(Game_Screen,Snake_Color,[i[0],i[1]],Snake_Size) #screen,color,position,radius
		#Draw_Snake() #draw the snake
		
		pygame.display.update()
		
		#make the snake grow when it eats food 
		if  (X_CoOrdinate_Start == Snake_Food_x) and (Y_CoOrdinate_Start == Snake_Food_y) :
			Snake_Food_x=round(random.randrange(0,800-10)/10.0) *10.0 #generate new food instead of the eaten one 
			Snake_Food_y=round(random.randrange(0,700-10)/10.0)*10.0
			Snake_Length += 1 #increase the length of the snake with 1
			#print("here")
			
		Game_Clock.tick(Snake_Speed) #delay to draw the next frame --> maps to the speed of the snake finally
		
	pygame.quit() #quit the game using pygame quit function
	quit()
#----------------------------------------------------
Window_1=Tk() #this window has got all the advantages of the tkinter gui library
Window_1.title("Hello from Snake Game") #title of the window
Window_1.geometry('800x700') #set the width and height of the window
Window_1.configure(bg='black')

photo_Snake = PhotoImage(file='Snake.png')
photo_Snake = photo_Snake.subsample(1,1) #columns,rows 
label_Snake= Label(Window_1, image = photo_Snake)
label_Snake.place(x=0,y=0)

label_Snake_Color = Label(Window_1, text="Choose Snake Color here", bd='8')
label_Snake_Color.place(x=30,y=250)
Snake_Color_BLACK=Button(Window_1, bg='BLACK' , bd='12',command=lambda :Snake_Color_Choosed(BLACK))
Snake_Color_BLACK.place(x=85,y=300)
Snake_Color_WHITE=Button(Window_1, bg='WHITE' , bd='12',command=lambda :Snake_Color_Choosed(WHITE))
Snake_Color_WHITE.place(x=85,y=350)
Snake_Color_GREEN=Button(Window_1, bg='GREEN' , bd='12',command=lambda :Snake_Color_Choosed(GREEN))
Snake_Color_GREEN.place(x=85,y=400)
Snake_Color_BLUE = Button(Window_1, bg='BLUE', bd='12',command=lambda: Snake_Color_Choosed(BLUE))
Snake_Color_BLUE.place(x=85,y=450)
Snake_Color_GRAY=Button(Window_1, bg='GRAY' , bd='12',command=lambda :Snake_Color_Choosed(GRAY))
Snake_Color_GRAY.place(x=85,y=500)
Snake_Color_RED=Button(Window_1, bg='RED' , bd='12',command=lambda :Snake_Color_Choosed(RED))
Snake_Color_RED.place(x=85,y=550)

label_Snake_Difficulty = Label(Window_1, text="Choose Game Difficulty here", bd='8')
label_Snake_Difficulty.place(x=600,y=250)
Snake_Difficulty_Amateur = Button(Window_1, text='Amateur',bd='12',command=lambda:Game_Difficulty_Choosed(25), bg='RED')
Snake_Difficulty_Amateur.place(x=650,y=300)
Snake_Difficulty_Normal = Button(Window_1, text='Normal',bd='12',command=lambda:Game_Difficulty_Choosed(35), bg='GRAY')
Snake_Difficulty_Normal.place(x=650,y=350)
Snake_Difficulty_Hard = Button(Window_1, text='Hard',bd='12',command=lambda:Game_Difficulty_Choosed(45), bg='BLUE')
Snake_Difficulty_Hard.place(x=656,y=400)
Snake_Difficulty_Pro = Button(Window_1, text='Professional',bd='12',command=lambda:Game_Difficulty_Choosed(65), bg='Green')
Snake_Difficulty_Pro.place(x=635,y=450)

Start_Button = Button(Window_1, text="Start",command=Game_Start, bd='15', bg='CYAN')
Start_Button.place(x=380,y=550)

Window_1.mainloop() #to run the window

if Game_Start_Flag==1:
	pygame.init() #intialize all imported modules of pygame lib
	Game_Clock= pygame.time.Clock()
	Game_Screen = pygame.display.set_mode((800,700)) #make a 800*800 screen 
	Game_Screen.fill(CYAN) #fill the screen with cyan color
	pygame.display.set_caption('Snake Game<3') #title of the screen
	Set_Snake_Color(Snake_Color)
	Set_Snake_Speed(Snake_Speed)
	Play_The_Game()