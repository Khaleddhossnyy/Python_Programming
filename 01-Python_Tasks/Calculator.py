#--------------------------------------------------------------------------------------------------
import numpy 
import goto
#--------------------------------------------------------------------------------------------------

#Make this calculator work forever
while 1:
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#let the user Enter the type of calculator he needs
	print()
	Calculator_Type = int(input("--> Enter 1 for Scientific calculator or 2 for progamming calculator : "))
	Calculator_Type_Code =[1,2]
	if Calculator_Type not in Calculator_Type_Code:
		print("!!!!!Invalid Mode, Please try again")
#--------------------------------------------------------------------------------------------------
#----------------------------------- Start of scientfic calculator --------------------------------

	if Calculator_Type == 1: #Scientific Calculator
		Mathematical_Expression = input("Enter the expression you want to evaluate : ")
		#print(Mathematical_Expression)
		while (1):
			try:
				print("Answer = %0.2f" %(eval(Mathematical_Expression)))  #changes the string to an executable expression and executes it
				break 
			except:
				print("!!!!!Invalid Expression, enter Again:")
				Mathematical_Expression = input ("Enter the expression you want to evaluate :")
		#Number_1,Number_2 = input("Enter two numbers to operate on :").split(" ",2) #taking the parameters from the user
		#print("here")
		#Operation = input("Please enter the operation you want to execute: ")  #taking the operation from the user
		#if Operation == '+': #summation
			#Summation = float(Number_1) + float(Number_2)
			#print("Summation of %0.2f and %0.2f equals: %0.2f" %(float(Number_1),float(Number_2),Summation))
			
		#elif Operation == '-': #difference
			#Difference = float(Number_1) - float(Number_2)
			#print("Difference of %0.2f and %0.2f equals: %0.2f" %(float(Number_1),float(Number_2),Difference))
		
		#elif Operation == '*': #multplication
			#Multplication = float(Number_1) * float(Number_2)
			#print("Multplication of %0.2f and %0.2f equals: %0.2f" %(float(Number_1),float(Number_2),Multplication))
		
		#elif Operation == '/': #division
			#Division = float(Number_1) / float(Number_2)
			#print("Division of %0.2f and %0.2f equals: %0.2f" %(float(Number_1),float(Number_2),Division))
		
		#elif Operation == '%': #modulus
			#Modulus = float(Number_1) % float(Number_2)
			#print("Modulus of %0.2f and %0.2f equals: %0.2f" %(float(Number_1),float(Number_2),Modulus))
			
#----------------------------------- End of scientfic calculator ----------------------------------
#--------------------------------------------------------------------------------------------------	
#----------------------------------- start of programming calculator ------------------------------
	elif Calculator_Type == 2: #progrmming calculator
	
		print("Enter 1 for Decimal --> Binary")
		print("Enter 2 for Decimal --> Hexa")
		print("Enter 3 for Binary --> Decimal")
		print("Enter 4 for Hexa --> Decimal")
		print("Enter 5 for Decimal --> Oct")
		print("Enter 6 for Oct --> Decimal")
		print("Enter 7 for << an integer")
		print("Enter 8 for >> an integer")
		
		Programming_Type_Code = [1,2,3,4,5,6,7,8]
		Programming_Type = int(input("--> Enter the number corresponding to your choice: "))
		
		Prog = 1    #to handle a non true choice 
		while(Prog):
		
			if Programming_Type == 1: #change from decimal to binary 
				Decimal_Number = int(input("--> Enter a decimal number : "))  #input any decimal number with no restrictions 
				Copy_Decimal_Number = Decimal_Number #to print it at the final phase 
				Counter=0  #for looping on the binary list
				Binary_Array=[] #list to save the binary bits in it
				Binary_Array.clear() #to remove anything from the list 
				#Binary_Array.pop(0) 
				while Decimal_Number > 0:  #calculating the binary bits
					Binary_Array.insert(Counter,int(Decimal_Number) % 2) #put the bit extracted in the binary array in the position of the counter
					Decimal_Number = int(Decimal_Number) /2
					Counter = Counter +1
				else:
					Binary_Array_length = len(Binary_Array)
					#print(Binary_Array_length)
					print("The binary Number corresponding to %d is 0b : " %(Copy_Decimal_Number), end =' ') 
					for n in range (Binary_Array_length,1,-1):  #print the binary array in reverse odrer to get the binary true number corresponding to the entered decimal number
						print(Binary_Array[n-2], end =' ')  #to print the binary bits along side each other 
					break
					
			elif Programming_Type == 2:  #change from decimal to hexa
				Decimal_Number = int(input("--> Enter a decimal number : "))  #input any decimal number with no restrictions 
				Copy_Decimal_Number = Decimal_Number #to print it at the final phase 
				Counter=0  #for looping on the binary list
				Hexa_Array=[] #list to save the binary bits in it
				Hexa_Array.clear() #to remove anything from the list 
				while Decimal_Number > 0:
					Remainder = int(Decimal_Number) % 16 #to get the hexadecimal bits
					#print(Remainder)
					if Remainder < 10:
						Hexa_Array.insert(Counter,Remainder)
						Decimal_Number=int(Decimal_Number)/16
						Counter = Counter + 1
						#print("Here")
					elif Remainder >= 10:
						#print("Here")
						Remainder = chr(Remainder + 55) #55+10= A , 55+11=B, 55+12=C , 55+13=D , 55+14=E, 55+15=f and chr to print the character corresponding to this ascci 
						#Remainder_Value = ord(Remainder)
						Hexa_Array.insert(Counter,Remainder)
						Decimal_Number=int(Decimal_Number)/16
						Counter = Counter + 1
				else:
					Hexa_Array_length = len(Hexa_Array)
					#print("inside here")
					#print(Hexa_Array_length)
					print("The Hexa Number corresponding to %d is 0X : " %(Copy_Decimal_Number), end =' ') 
					for n in range (Hexa_Array_length,1,-1):  #print the hexa array in reverse odrer to get the Hexa true number corresponding to the entered decimal number
						print(Hexa_Array[n-2], end =' ')  #to print the hexa bits along side each other
					break	
			
			elif Programming_Type == 3: #change from binary to decimal
				Binary_Array=[0];
				Binary_Array = input("--> Please enter the binary Number separated by spaces: ").split(" ")
				Binary_Array_length = len(Binary_Array)
				Decimal_Number=0
				#print(Binary_Array_length)
				for n in range(0,Binary_Array_length,1):
					if Binary_Array[n] == '1': #compare a string with a string 
						Decimal_Number = int(Decimal_Number) + (2**(Binary_Array_length - n -1)) #2^0 = 2^binary_Array_length-1 , 2^1 = 2 ^binary_Array_length-2
						print(Decimal_Number)
					if Binary_Array[n] == '0': 
						Decimal_Number = int(Decimal_Number) +0 #if bit equals zero add nothing to the summation
					if Binary_Array_length-1 == n:  
						Decimal_Number = Decimal_Number + (2**(Binary_Array_length - n -1)-1) #2^7=255 instead of 256
						#print(Decimal_Number)
				print("The decimal number corresponding to this binary sequence  is : %d" %(Decimal_Number))
				break
			
			elif Programming_Type ==4: #change from hexa to decimal 
				Hexa_string = input("--> Please enter your hexadecimal number : ") #recieve the hexa number as a string 
				#print(Hexa_string)
				Decimal_Number = int(Hexa_string,16) #using int with argument 16 can convert a string to base 16 number and decimal at the same time
				print("The Decimal Number Corresponding to %s is %d " %(Hexa_string,Decimal_Number))
				break
			
			elif Programming_Type ==5: #change from decimal to oct
				Decimal_Number= int(input ("--> Please enter your decimal number: "))
				Octal_String = oct(Decimal_Number) #function to convert from decimal to oct
				print("The octal number corresponding to %d is %s " %(Decimal_Number,Octal_String))
				break
				
			elif Programming_Type ==6: #change from oct to decimal
				Octal_String = input("--> Please enter your octal number : ")
				Decimal_Number = int(Octal_String,8)
				print("The decimal number corresponding to %s is %d " %(Octal_String,Decimal_Number))
				break
				
			elif Programming_Type ==7: #shift left
				Decimal_Number = int(input("--> Please enter your decimal number : "))
				Number_of_shifts = int(input(" --> Please enter how many shifts you want : "))
				Decimal_Number_Shifted = Decimal_Number << Number_of_shifts
				print("The decimal number after shifting left %d times is %d"%(Number_of_shifts,Decimal_Number_Shifted))
				break
				
			
			elif Programming_Type ==8: #shift right
				Decimal_Number = int(input("--> Please enter your decimal number : "))
				Number_of_shifts = int(input(" --> Please enter how many shifts you want : "))
				Decimal_Number_Shifted =float(Decimal_Number >> Number_of_shifts)
				print("The decimal number after shifting right %d times is %0.2f"%(Number_of_shifts,Decimal_Number_Shifted))	
				break

			elif Programming_Type not in Programming_Type_Code:
				print("XXXX You entered a wrong choice, try again")
				print("Enter 1 for Decimal --> Binary")
				print("Enter 2 for Decimal --> Hexa")
				print("Enter 3 for Binary --> Decimal")
				print("Enter 4 for Hexa --> Decimal")
				print("Enter 5 for Decimal --> Oct")
				print("Enter 6 for Oct --> Decimal")
				print("Enter 7 for << an integer")
				print("Enter 8 for >> an integer")
				#Programming_Type_Code = [1,2,3,4,5,6,7,8]
				Programming_Type = int(input("--> Enter the number corresponding to your choice: "))
				prog = 0 #like a goto label but with while loop because goto destroys the structure of the program
			
#----------------------------------- End of programming calculator --------------------------------		
#--------------------------------------------------------------------------------------------------	