import sys,time,os,colorama
os.system("") #without it ansi escape sequences don't work on my pc
#---------------------------------------------------------------------------
#-----------------------------Create positioning function ------------------
def pos (x,y) : #{
	return '\x1b[' + str(y) +';'+ str(x) + 'H';  #ANSI escape sequence which chnages the cursor location according to the given co-ordinates where specs are:{Column,Row}
#}
#---------------------------------------------------------------------------
#----------------------------- Take number of stars ------------------------
#---------------------------------------------------------------------------
Number_Of_Rows = int(input("Enter number of Rows: "))
#---------------------------------------------------------------------------
#---------------------------- Drawing the initial triangle -----------------
for i in range(0,Number_Of_Rows): #this for loop will make the rows
	print(pos(1,6+i),end=' ') #for all the triangles to be constructed in the same way , the first triangle all rows start from the first column , and row 6
	for j in range (0,i+1): #this for loop will be concered with drawing the right amount of stars in each row
		print("*", end='')
	#print("\n") #after finishing each row go to the next row
	print() 
time.sleep(0.5)
#---------------------------- End Drawing the initial triangle---------------
#----------------------------------------------------------------------------
#----------------------------- Rotating the triangle ------------------------

#------------------------------------first rotation--------------------------
#for i in range(0,Number_Of_Rows+2):
	#sys.stdout.write("\033[A")  #return the cursor to the beginning of the previous line but it deletes what was previously printed on this line
	#print(end=" ")
#sys.stdout.write("\033[<0>;<4>H")
for i in range(0,Number_Of_Rows):
	for j in range(i,Number_Of_Rows): #to print a number of stars = the number of the row we are standing in at the momment
		print(pos(4+j,6+i),end='') #set the cursor at this location 
		print("*",end='')
	#print("\n")
	print()
time.sleep(0.5) 
#--------------------------------End first rotation--------------------------

#---------------------------------Line forming-------------------------------
for i in range(0,Number_Of_Rows):
	print(pos(Number_Of_Rows+6,6+i),end='')
	print("*")  #prints a straight line of stars bottom down from the starting row
print()
time.sleep(0.5)
#--------------------------------End Line forming----------------------------

#-----------------------------------Second rotation--------------------------
for i in range (0,Number_Of_Rows):
	print(pos(Number_Of_Rows+9,6+i),end='')
	for j in range(i,Number_Of_Rows): #to print a number of stars = the number of the row we are standing in at the momment
		print("*",end='')
	print()
time.sleep(0.5)
#----------------------------------------------------------------------------

#------------------------------------Third rotation--------------------------
for i in range(0,Number_Of_Rows):
	for j in range(0,i+1): #to print a number of stars = the number of the row we are standing in at the momment
		print(pos((Number_Of_Rows*2+10)-j,6+i),end='') #set the cursor at this location 
		print("*",end='')
	#print("\n")
	print()
time.sleep(0.5) 
#------------------------------End third rotation----------------------------

#------------------------------Second Line formation--------------------------
for i in range(0,Number_Of_Rows*2+10-1):
	print(pos(i+2,6+Number_Of_Rows), end='')
	print("*",end='')
print()
time.sleep(0.5)
#sys.stdout.write("\033[2J") #for clearing the screen
#------------------------------End second line formation----------------------

#---------------------------------------Fourth rotation-----------------------
for i in range (0,Number_Of_Rows):
	print(pos(2,6+Number_Of_Rows+i+1),end='')
	for j in range(i,Number_Of_Rows): #to print a number of stars = the number of the row we are standing in at the momment
		print("*",end='')
	print()
time.sleep(0.5)	
#------------------------------end fourth rotation----------------------------

#---------------------------------fifth rotation------------------------------
for i in range(0,Number_Of_Rows):
	for j in range(0,i+1): #to print a number of stars = the number of the row we are standing in at the momment
		print(pos((Number_Of_Rows+3)-j,6+i+1+Number_Of_Rows),end='') #set the cursor at this location 
		print("*",end='')
	#print("\n")
	print()
time.sleep(0.5) 
#sys.stdout.write("\033[2J") #for clearing the screen
#--------------------------------end fifth rotation---------------------------

#----------------------------------Third line formation-----------------------
for i in range(0,Number_Of_Rows):
	print(pos(Number_Of_Rows+6,6+i+1+Number_Of_Rows),end='')
	print("*")  #prints a straight line of stars bottom down from the starting row
print()
time.sleep(0.5)
#sys.stdout.write("\033[2J") #for clearing the screen
#--------------------------------End third line formation---------------------

#-------------------------------Sixth rotation--------------------------------
for i in range(0,Number_Of_Rows): #this for loop will make the rows
	print(pos(Number_Of_Rows+6+2,6+i+1+Number_Of_Rows),end=' ') #for all the triangles to be constructed in the same way , the first triangle all rows start from the first column , and row 6
	for j in range (0,i+1): #this for loop will be concered with drawing the right amount of stars in each row
		print("*", end='')
	#print("\n") #after finishing each row go to the next row
	print() 
time.sleep(0.5)
#------------------------------End sixth rotation-----------------------------

#-----------------------------seventh rotation--------------------------------
for i in range(0,Number_Of_Rows):
	for j in range(i,Number_Of_Rows): #to print a number of stars = the number of the row we are standing in at the momment
		print(pos(j+Number_Of_Rows+6+5,6+i+1+Number_Of_Rows),end='') #set the cursor at this location 
		print("*",end='')
	#print("\n")
	print()
time.sleep(10)
sys.stdout.write("\033[2J") #for clearing the screen
print(pos(0,1)) #to put the cursor at the top again for the next run
#-----------------------------End seventh rotation----------------------------


#----------------------------- End rotating the triangle ---------------------
#-----------------------------------------------------------------------------