import sys,time,os,colorama
os.system("") #without it ansi escape sequences don't work on my pc
#---------------------------------------------------------------------------
#-----------------------------Create positioning function ------------------
def pos (x,y) : #{
	return '\x1b[' + str(y) +';'+ str(x) + 'H';  #ANSI escape sequence which chnages the cursor location according to the given co-ordinates where specs are:{Column,Row}
#}
#---------------------------------------------------------------------------
#----------------------------Drawing the initial arrow ---------------------
while 1:
	sys.stdout.write("\033[2J")
	for i in range(0,15):
		print(pos(35+i,15),end='')
		print("*",end='')
	print()
	#time.sleep(2)

	for i in range(0,6): #this for loop will make the rows
		print(pos(50,10+i),end=' ') #for all the triangles to be constructed in the same way , the first triangle all rows start from the first column , and row 6
		for j in range (0,i+1): #this for loop will be concered with drawing the right amount of stars in each row
			print("*", end='')
		#print("\n") #after finishing each row go to the next row
		print() 
	#time.sleep(2)

	for i in range(0,6): #this for loop will make the rows
		print(pos(50,16+i),end=' ') #for all the triangles to be constructed in the same way , the first triangle all rows start from the first column , and row 6
		for j in range (i,6): #this for loop will be concered with drawing the right amount of stars in each row
			print("*", end='')
		#print("\n") #after finishing each row go to the next row
		print() 
	time.sleep(0.2)
#---------------------------End drawing the initial arrow-------------------

#----------------------------First rotaion---------------------------------
	sys.stdout.write("\033[2J") #clear the screen
	for i in range(0,8):
		print(pos(35,15-i),end='')
		print("*")
	print()
	#time.sleep(2)
	
	for i in range(0,12): #first line of the triangle 
		print(pos(29+i,7),end='')
		print("* ", end =' ')
	print()
	#time.sleep(4)
	
	for i in range(0,10): #second
		print(pos(30+i,6),end='')
		print("*")
	print()
	
	for i in range(0,8): #third
		print(pos(31+i,5),end='')
		print("*")
	print()
	
	for i in range(0,6): #fourth
		print(pos(32+i,4),end='')
		print("*")
	print()
	
	for i in range(0,4): #fiifth
		print(pos(33+i,3),end='')
		print("*")
	print()
	
	for i in range(0,2): #sixth
		print(pos(34+i,2),end='')
		print("*")
	print()
	time.sleep(0.2)
#--------------------------End first rotation-------------------------------
#--------------------------second rottaion ---------------------------------
	sys.stdout.write("\033[2J")
	for i in range(0,15):
		print(pos(35-i,15),end='')
		print("*",end='')
	print()
	#time.sleep(2)
	for i in range(0,6):
		for j in range(0,i+1): #to print a number of stars = the number of the row we are standing in at the momment
			print(pos(19-j,10+i),end='') #set the cursor at this location 
			print("*",end='')
		#print("\n")
		print()
	#time.sleep(1) 

	for i in range(0,5):
		for j in range(i,5): #to print a number of stars = the number of the row we are standing in at the momment
			print(pos(j+15,16+i),end='') #set the cursor at this location 
			print("*",end='')
	#print("\n")
	print()
	time.sleep(0.2)
	#sys.stdout.write("\033[2J") #for clearing the screen
	#print(pos(0,1)) #to put the cursor at the top again for the next run
#-------------------------End second rotation ------------------------------
#-------------------------- third rotation ---------------------------------
	sys.stdout.write("\033[2J") #clear the screen
	for i in range(0,8):
		print(pos(35,15+i),end='')
		print("*")
	print()
	#time.sleep(2)
	
	for i in range(0,12): #first line of the triangle 
		print(pos(29+i,23),end='')
		print("* ", end =' ')
	print()
	#time.sleep(4)
	
	for i in range(0,10): #second
		print(pos(30+i,24),end='')
		print("*")
	print()
	
	for i in range(0,8): #third
		print(pos(31+i,25),end='')
		print("*")
	print()
	
	for i in range(0,6): #fourth
		print(pos(32+i,26),end='')
		print("*")
	print()
	
	for i in range(0,4): #fiifth
		print(pos(33+i,27),end='')
		print("*")
	print()
	
	for i in range(0,2): #sixth
		print(pos(34+i,28),end='')
		print("*")
	print()
	time.sleep(0.2)
#-------------------------End third rotation -------------------------------

