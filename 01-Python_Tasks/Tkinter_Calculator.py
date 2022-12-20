from tkinter import * 
#--------------------------------------------------------------------------------
Input_Expression = "" #this will hold the expression which we need to execute 
#---------------------------------------------------------------------------------
def A_Number_Operation_Pressed(Number):
	global Input_Expression #global to be able to change the input expression which the whole program sees
	Input_Expression = Input_Expression + str(Number) #concatinate the pressed number with the previously pressed numbers and operations
	equation.set(Input_Expression)
#---------------------------------------------------------------------------------
def Equal_Pressed():
	try:
		global Input_Expression
		Result = str(eval(Input_Expression)) 
		equation.set(Result)
		Input_Expression = "" #so that the result will appear alone after pressing equal 
	#finally:
	except:
		equation.set("There is an error in the entered expression to be executed")
		Input_Expression = "" 
#--------------------------------------------------------------------------------
def AC_Pressed():
	global Input_Expression
	Input_Expression = "" #this will hold the expression which we need to execute 
	equation.set("")
#--------------------------------------------------------------------------------
Window_1=Tk() #this window has got all the advantages of the tkinter gui library
Window_1.title("Hello from tkinter") #title of the window
Window_1.geometry('500x400') #set the width and height of the window
Window_1.configure(bg='black')
#-------------------------- Operations buttons------------------------------------
#lambda allows the sending of multiple data trhough function call back
Button_ADD = Button(Window_1 , text = "+" , bd = '10',bg='red', fg='black',command=lambda:A_Number_Operation_Pressed("+"))
Button_ADD.place(x=350,y=150)

Button_Subtract = Button(Window_1 , text = "- " , bd = '10',bg='red', fg='black',command=lambda: A_Number_Operation_Pressed("-"))
Button_Subtract.place(x=350,y=200)

Button_Mul = Button(Window_1 , text = "* " , bd = '10',bg='red', fg='black',command=lambda: A_Number_Operation_Pressed("*"))
Button_Mul.place(x=350,y=250)

Button_Div = Button(Window_1 , text = "/ " , bd = '10',bg='red', fg='black',command=lambda: A_Number_Operation_Pressed("/"))
Button_Div.place(x=350,y=300)

#----------------------------- Number buttons------------------------------------
Button_1 = Button(Window_1 , text = "1 " , bd = '10',bg='red', fg='black',command=lambda: A_Number_Operation_Pressed(1))
Button_1.place(x=100,y=150)

Button_2 = Button(Window_1 , text = "2 " , bd = '10',bg='red', fg='black',command=lambda: A_Number_Operation_Pressed(2))
Button_2.place(x=150,y=150)

Button_3 = Button(Window_1 , text = "3 " , bd = '10',bg='red', fg='black',command=lambda: A_Number_Operation_Pressed(3))
Button_3.place(x=200,y=150)

Button_4 = Button(Window_1 , text = "4 " , bd = '10',bg='red', fg='black',command=lambda: A_Number_Operation_Pressed(4))
Button_4.place(x=100,y=200)

Button_5 = Button(Window_1 , text = "5 " , bd = '10',bg='red', fg='black',command=lambda: A_Number_Operation_Pressed(5))
Button_5.place(x=150,y=200)

Button_6 = Button(Window_1 , text = "6 " , bd = '10',bg='red', fg='black',command=lambda: A_Number_Operation_Pressed(6))
Button_6.place(x=200,y=200)

Button_7 = Button(Window_1 , text = "7 " , bd = '10',bg='red', fg='black',command=lambda: A_Number_Operation_Pressed(7))
Button_7.place(x=100,y=250)

Button_8= Button(Window_1 , text = "8 " , bd = '10',bg='red', fg='black',command=lambda: A_Number_Operation_Pressed(8))
Button_8.place(x=150,y=250)

Button_9 = Button(Window_1 , text = "9 " , bd = '10',bg='red', fg='black',command=lambda: A_Number_Operation_Pressed(9))
Button_9.place(x=200,y=250)

Button_0 = Button(Window_1 , text = "0 " , bd = '10',bg='red', fg='black',command=lambda: A_Number_Operation_Pressed(0))
Button_0.place(x=100,y=300)

Button_Ac = Button(Window_1 , text = "Ac" , bd = '10',bg='red', fg='black',command=AC_Pressed)
Button_Ac.place(x=150,y=300)

Button_eq = Button(Window_1 , text = "= " , bd = '10',bg='red', fg='black',command=Equal_Pressed)
Button_eq.place(x=200,y=300)

Button_des = Button(Window_1, text="   Exit   ", bd='8' ,command = Window_1.destroy)
Button_des.place(x=20,y=52)
#------------------------------------------------------------------------------------
#-------------------------------------- entry ---------------------------------------
L1 = Label(Window_1, text="Enter Numbers : ", bd='10')
L1.place(x=100,y=52)

equation = StringVar() #String_Var is a variable class which will be used here so  i created an object from it in this line

E1 = Entry(Window_1, bd ='5', textvariable=equation,font="Georgia 15") #linkong the entrey with the input expression because in the functions equation is related to the expression
E1.place(x=220,y=52)
#------------------------------------------------------------------------------------
Window_1.mainloop() #to run the window 