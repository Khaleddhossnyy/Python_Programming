#---------------------------------------------------------
import linecache
from datetime import datetime
#---------------------------------------------------------
print("<3 Wlecome to Our ITI Shop <3")
#---------------------------------------------------------
owner =0
user=0
sum=0
New_Amount_Flag=0
#---------------------------------------------------------
#------------------Defining ITI shop dict----------------
ITI_Shop_Dict={} #iti dictionary of grocery which will be filled from the grocery part of the database
counter=1
Grocery_Part = open("ITI_Shop_Grocery.txt","r")
Grocery_Part_Lines_Count=len(Grocery_Part.readlines())
Grocery_Part.close()
Grocery_Part = open("ITI_Shop_Grocery.txt","r")
#print(Grocery_Part_Lines_Count)
for i in range (0,Grocery_Part_Lines_Count):
	Grocery_Part_Line = Grocery_Part.readline()
	ITI_Shop_Dict[Grocery_Part_Line[Grocery_Part_Line.find("-")+1 :Grocery_Part_Line.rfind("-")]]= [ Grocery_Part_Line[Grocery_Part_Line.find("*")+1:Grocery_Part_Line.rfind("*")] , Grocery_Part_Line[Grocery_Part_Line.find("(")+1:Grocery_Part_Line.rfind(")") ],Grocery_Part_Line[Grocery_Part_Line.find("%")+1:Grocery_Part_Line.rfind("%")]]
print(ITI_Shop_Dict)
#------------End Defining ITI shop dict------------------
while 1: #to make this system work forever
#---------------------------------------------------------
#---------------------------------------------------------
#-------------------Choosing the mode---------------------
	print("--------------------------------------------------------------")
	print("Enter 1 for Owner mode")
	print("Enter 2 for User/Client mode")
	print("Enter 0 to exit")
	
	Operation_Mode = int(input("--> Enter the number of the desired mode please: ")) #recieve the operation mode
	Operation_Mode_code =[0,1,2] #list with the available operation modes
	
	if Operation_Mode not in Operation_Mode_code: #to handle wrong input choice
		print("!!!!! Invalid Mode, Please try again")
	
	elif Operation_Mode == 0:   #close the program
		print("Bye,Hope to see you here again, soon <3")
		break
		
	elif Operation_Mode == 1: #owner mode
		Owners_Name_List =["Khaled"]
		Owners_Password_List = [1234]
		Owner_Name = input("Please Enter your name here: ") #the owner is Khaled for starters 
		Owner_Password = int(input("Please Enter your password here: "))
		
		if Owner_Name in Owners_Name_List:
			Owner_Name_Index = Owners_Name_List.index(Owner_Name) #get the index of this owner name in the owners names list
			if Owners_Password_List [Owner_Name_Index] == Owner_Password: #if the owner password entered equals the one saved to his name then proceed 
				#print("This owner exist")   #the owner's code starts here
				owner =1 #approved owner flag
			else:
				while (1): #keep trying to enter the right password 
					print("!!!! Incorrect password, please enter the correct password")
					Owner_Password = int(input("Please Enter your password here:"))
					if Owners_Password_List [Owner_Name_Index] == Owner_Password:
						#print("finally true")
						owner =1 #approved owner flag
						break
						
		elif (Owner_Name not in Owners_Name_List) and (Owner_Password not in Owners_Password_List):
			while(1):
				print("!!!! The owner name or the password is incorrect please enter both again")
				Owner_Name = input("Please Enter your name here: ")
				Owner_Password = int(input("Please Enter your password here:"))
				#Owner_Name_Index = Owners_Name_List.index(Owner_Name) #get the index of this owner name in the owners names list
				if Owner_Name in Owners_Name_List:
					Owner_Name_Index = Owners_Name_List.index(Owner_Name) #get the index of this owner name in the owners names list
					if Owners_Password_List [Owner_Name_Index] == Owner_Password:
						#print("Here")
						owner=1
						break				
						
		
		elif Owner_Name not in Owners_Name_List:
			while(1):
				print("!!!! Incorrect Owner name, Please Enter your correct name")
				Owner_Name = input("Please Enter your name here: ")
				if Owner_Name in Owners_Name_List:
					#print("finally") 
					owner =1 #approved owner flag
					break
	
	elif Operation_Mode ==2: #client mode
		user=1 #approved user flag 
#-----------------end choosing the mode------------------
#--------------------------------------------------------
#------------------Operation based on each mode----------
	if owner ==1: #we are operating in the admin mode
		while(1):
			print("--------------------------------------------------------------")
			print("Press 1 for Adding new products")
			print("Press 2 for showing the existing products")
			print("Press 3 for changing cost of a product")
			print("Press 4 for getting a certain grocery section from the database")
			print("Press 5 for sadly firing an employee and documenting this in a database")
			print("Press 0 to exit to previus menu")
			
			Owner_Choice = int(input("--> Enter the number corresponding to the desired operation: "))
			Owner_choice_Code=[0,1,2,3,4,5]
			
			if Owner_Choice not in Owner_choice_Code:
				while(1):
					print("!!!! Invalid option,Please enter a valid one")
					Owner_Choice = int(input("--> Enter the number corresponding to the desired operation: "))
					if Owner_Choice in Owner_choice_Code:
						Owner_Choice =Owner_choice_Code 
						break
			
			if Owner_Choice == 1: #adding new products
				New_Item = input("Enter the new item's name here: ")
				New_Item_Kilos = int(input("Enter the number of kilos of this item here: "))
				New_Item_Price = int(input("Enter the new item's price of one kilo here: "))
				Grocery_Part = open("ITI_Shop_Grocery.txt","a+")
				Grocery_Part.write("\n")
				Grocery_Part.write("-%s- : *%d* , (%d) ,%0%"  %(New_Item,New_Item_Kilos,New_Item_Price))
				Grocery_Part.close()
				Grocery_Part = open("ITI_Shop_Grocery.txt","r")
				Grocery_Part_Lines_Count=len(Grocery_Part.readlines())
				Grocery_Part.close()
				Grocery_Part = open("ITI_Shop_Grocery.txt","r")
				for i in range (0,Grocery_Part_Lines_Count):
					Grocery_Part_Line = Grocery_Part.readline()
					ITI_Shop_Dict[Grocery_Part_Line[Grocery_Part_Line.find("-")+1 :Grocery_Part_Line.rfind("-")]]= [ Grocery_Part_Line[Grocery_Part_Line.find("*")+1:Grocery_Part_Line.rfind("*")] , Grocery_Part_Line[Grocery_Part_Line.find("(")+1:Grocery_Part_Line.rfind(")")],Grocery_Part_Line[Grocery_Part_Line.find("%")+1:Grocery_Part_Line.rfind("%")]]
				print(ITI_Shop_Dict)
				Grocery_Part.close()
				#print("The new Grocery of our shop is: ")
				#print(ITI_Shop_Dict)
				while(1):
					Add_Again= input("Do you want to add something else: Y/N?")
					if Add_Again == 'N':
						#print(ITI_Shop_Dict)
						break
					elif Add_Again == 'Y':
						New_Item = input("Enter the new item's name here: ")
						New_Item_Kilos = int(input("Enter the number of kilos of this item here: "))
						New_Item_Price = int(input("Enter the new item's price of one kilo here: "))
						Grocery_Part = open("ITI_Shop_Grocery.txt","a+")
						Grocery_Part.write("\n")
						Grocery_Part.write("-%s- : *%d* , (%d)" %(New_Item,New_Item_Kilos,New_Item_Price))
						Grocery_Part.close()
						Grocery_Part = open("ITI_Shop_Grocery.txt","r")
						Grocery_Part_Lines_Count=len(Grocery_Part.readlines())
						Grocery_Part.close()
						Grocery_Part = open("ITI_Shop_Grocery.txt","r")
						for i in range (0,3):
							Grocery_Part_Line = Grocery_Part.readline()
							ITI_Shop_Dict[Grocery_Part_Line[Grocery_Part_Line.find("-")+1 :Grocery_Part_Line.rfind("-")]]= [ Grocery_Part_Line[Grocery_Part_Line.find("*")+1:Grocery_Part_Line.rfind("*")] , Grocery_Part_Line[Grocery_Part_Line.find("(")+1:Grocery_Part_Line.rfind(")")], Grocery_Part_Line[Grocery_Part_Line.find("%")+1:Grocery_Part_Line.rfind("%")]]
						print(ITI_Shop_Dict)
						#print("The new Grocery of our shop is: ")
						#print(ITI_Shop_Dict)
			
			elif Owner_Choice == 2: #Show products 
				#print(ITI_Shop_Dict)
				for key, value in ITI_Shop_Dict.items():
					print ("There exist in our store,%0.2f kilos of %s and each kilo is priced with %d LE"%(value[0],key, value[1])) 
			
			
			elif Owner_Choice ==3: #change cost 
				New_Cost_Item = input("Enter the item you want to chnage it's cost: ")
				New_Cost =int(input("Enter the new cost of the kilo of this item: "))
				New_Kilos = int(input("Enter the new number of the kilos of this item: "))
				Grocery_Part = open("ITI_Shop_Grocery.txt","a+")
				Grocery_Part.write("\n")
				Grocery_Part.write("-%s- : *%d* , (%d)" %(New_Cost_Item,New_Kilos,New_Cost))
				Grocery_Part.close()
				Grocery_Part = open("ITI_Shop_Grocery.txt","r")
				Grocery_Part_Lines_Count=len(Grocery_Part.readlines())
				Grocery_Part.close()
				Grocery_Part = open("ITI_Shop_Grocery.txt","r")
				for i in range (0,Grocery_Part_Lines_Count):
					Grocery_Part_Line = Grocery_Part.readline()
					ITI_Shop_Dict[Grocery_Part_Line[Grocery_Part_Line.find("-")+1 :Grocery_Part_Line.rfind("-")]]= [ Grocery_Part_Line[Grocery_Part_Line.find("*")+1:Grocery_Part_Line.rfind("*")] , Grocery_Part_Line[Grocery_Part_Line.find("(")+1:Grocery_Part_Line.rfind(")")], Grocery_Part_Line[Grocery_Part_Line.find("%")+1:Grocery_Part_Line.rfind("%")]]
				print(ITI_Shop_Dict)
				Grocery_Part.close()
			
			elif Owner_Choice == 4: #getting a ceratin part from the database 
				Desired_Section = input("Enter the name of the Grocery Section you want to access : ")
				#print(Desired_Section)
				Selling_Part = open("ITI_Shop_Selling.txt","r")
				Selling_Part_Lines_Count=len(Selling_Part.readlines())
				#print(Selling_Part_Lines_Count)
				Grocery_Part.close()
				Selling_Part = open("ITI_Shop_Selling.txt","r")
				for i in range(0,Selling_Part_Lines_Count):
					Selling_Part_Line = Selling_Part.readline()
					#print(Selling_Part_Line)
					if Desired_Section in Selling_Part_Line :
						print(Selling_Part_Line)
			
			elif Owner_Choice ==5: #firing an employee
				Employee_List=[]
				Employees_Part = open("ITI_Shop_Employees.txt","r")
				Employees_Part_Lines_Count=len(Employees_Part.readlines())
				Employees_Part.close()
				Employees_Part = open("ITI_Shop_Employees.txt","r")
				print("----ITI Shop Current Employees are : ----")
				for i in range(0,Employees_Part_Lines_Count):
					#Employees_Part.readline()
					Employee_List.append(Employees_Part.readline())
				print(Employee_List)
				Employees_Part.close()
				Line_Number=1
				Employees_Part = open("ITI_Shop_Employees.txt","r")
				To_Be_Fired_Employee = input("Type the name of the employee to be fired : ")
				for i in range(0,Employees_Part_Lines_Count+1):
					Employees_Part_Line = Employees_Part.readline()
					#print(Employees_Part_Line)
					if Employees_Part_Line.find(To_Be_Fired_Employee) != -1:
						Line_Number=i
						#print("here from break")
						break
					else:
						#print("HERE")
						Line_Number = Line_Number+1
						if (Line_Number >Employees_Part_Lines_Count ):
							print("Employee not found")
						
				print(Line_Number)
				Employees_Part.close()
				Employees_Part = open("ITI_Shop_Employees.txt","r")
				Employees_Part_NEW= Employees_Part.readlines()
				Employees_Part.close()
				Employees_Part = open("ITI_Shop_Employees.txt","r")
				Employees_Part_Fired = Employees_Part.readlines()
				Employees_Part.close()
				Fired_Employee = 'The Employee : ' + str(To_Be_Fired_Employee) + ' is fired At : ' + str(datetime.now())
				Employees_Part_NEW[Line_Number] =""
				#Employees_Part_NEW[Line_Number+1] = ""
				#Employees_Part.close()
				Employees_Part = open("ITI_Shop_Employees.txt","w")   
				for line in Employees_Part_NEW:
					Employees_Part.write(line)
					Employees_Part.write("\n")
				Employees_Part.close()
				Fired_Employee_Part=open("ITI_Shop_Fired_Employees.txt","a+")
				#print(Employees_Part_Fired)
				Fired_Employee_Part.write('The Employee : ' + str(To_Be_Fired_Employee) + ' is fired At : ' + str(datetime.now()))
				Fired_Employee_Part.write("\n")
				print("!!!!!! Employee fired")
				Fired_Employee_Part.close()
			
			elif Owner_Choice ==0: #return to the previous page
				owner =0
				break
	
	elif user ==1: #user mode on
		User_Name = input("Please Enter your name here : ")
		while(1):
			print("--------------------------------------------------------------")
			print("Press 1 for showing products in store")
			print("Press 2 for buying from the existing products")
			print("Press 3 for printing your bill")
			print("Press 0 to exit to previus menu")
			
			Customer_Choice = int(input("--> Enter the number corresponding to the desired operation: "))
			Customer_choice_Code=[0,1,2,3]
			
			if Customer_Choice not in Customer_choice_Code:
					while(1):
						print("!!!! Invalid option,Please enter a valid one")
						Customer_Choice = int(input("--> Enter the number corresponding to the desired operation: "))
						if Customer_Choice in Customer_choice_Code:
							Customer_Choice = Customer_choice_Code 
							break
			if Customer_Choice == 1: #show products
				for key, value in ITI_Shop_Dict.items():
						print ("There exist in our store,%0.2f kilos of %s and each kilo is priced with %d LE"%(int(value[0]),key, int(value[1]))) 
			
			if Customer_Choice ==2 : #buy products
				
				To_Buy = input("Enter the name of the item you want to buy: ")
				if To_Buy not in ITI_Shop_Dict:
					while(1):
						print("Sorry, this item is not available right now")						
						To_Buy = input("Enter the name of the item you want to buy: ")
						#Buy_Flag =0
						if To_Buy in ITI_Shop_Dict:
							#Buy_Flag=1
							break
				index_To_Buy = list(ITI_Shop_Dict).index(To_Buy)
				
				if  ITI_Shop_Dict[To_Buy][0] == 0 :
					while(1):
						print("Sorry, we just ran out of this item")
						To_Buy = input("Enter the name of the item you want to buy: ")
						if To_Buy not in ITI_Shop_Dict:
							while(1):
								print("Sorry, this item is not available right now")						
								To_Buy = input("Enter the name of the item you want to buy: ")
								#Buy_Flag =0
								if To_Buy in ITI_Shop_Dict:
									#Buy_Flag=1
									break
						if To_Buy in ITI_Shop_Dict and ITI_Shop_Dict[To_Buy][0] != 0:
							print("here")
							break
				
				To_Buy_Amount= float(input("Please enter how many kilos do you want of this item: "))
				if To_Buy_Amount <= int(ITI_Shop_Dict[To_Buy][0]) :
					New_Amount= int(ITI_Shop_Dict[To_Buy][0]) - To_Buy_Amount
					ITI_Shop_Dict[To_Buy][0]=New_Amount
					ITI_Shop_Dict[To_Buy][2]=To_Buy_Amount
					sum = sum + To_Buy_Amount *int(ITI_Shop_Dict[To_Buy][1])
					Selling_Part = open("ITI_Shop_Selling.txt","a+")
					Selling_Part.write("\n")
					Selling_Part.write("Customer -%s- : has bought *%0.2f* Kilos of (%s)" %(User_Name,To_Buy_Amount,To_Buy) + " At " +str(datetime.now()))
					Selling_Part.close()
					New_Amount_Flag=1
				else:
					print("!!!!!!The amount you are asking for isn't available at the moment sadly ")
				while(1):
					Add_Again= input("Do you want to Buy something else: Y/N?")
					if Add_Again == 'N':
						#print(ITI_Shop_Dict)
						break
					elif Add_Again == 'Y':
						To_Buy = input("Enter the name of the item you want to buy: ")
						if To_Buy not in ITI_Shop_Dict:
							while(1):
								print("Sorry, this item is not available right now")						
								To_Buy = input("Enter the name of the item you want to buy: ")
								#Buy_Flag =0
								if To_Buy in ITI_Shop_Dict:
									#Buy_Flag=1
									break
						index_To_Buy = list(ITI_Shop_Dict).index(To_Buy)
						
						if  int(ITI_Shop_Dict[To_Buy][0]) == 0 :
							while(1):
								print("Sorry, we just ran out of this item")
								To_Buy = input("Enter the name of the item you want to buy: ")
								if To_Buy not in ITI_Shop_Dict:
									while(1):
										print("Sorry, this item is not available right now")						
										To_Buy = input("Enter the name of the item you want to buy: ")
										#Buy_Flag =0
										if To_Buy in ITI_Shop_Dict:
											#Buy_Flag=1
											break
								if To_Buy in ITI_Shop_Dict and int(ITI_Shop_Dict[To_Buy][0] != 0):
									print("here")
									break
						
						To_Buy_Amount= float(input("Please enter how many kilos do you want of this item: "))
						if To_Buy_Amount <= int(ITI_Shop_Dict[To_Buy][0]) :
							New_Amount= float(ITI_Shop_Dict[To_Buy][0]) - float(To_Buy_Amount)
							ITI_Shop_Dict[To_Buy][0]=New_Amount
							ITI_Shop_Dict[To_Buy][2]=To_Buy_Amount
							sum = sum + To_Buy_Amount *int(ITI_Shop_Dict[To_Buy][1])
							Selling_Part = open("ITI_Shop_Selling.txt","a+")
							Selling_Part.write("\n")
							Selling_Part.write("Customer -%s- : has bought *%0.2f* Kilos of (%s)" %(User_Name,To_Buy_Amount,To_Buy) + " At " +str(datetime.now()))
							Selling_Part.close()
							New_Amount_Flag=1
						else:
							print("!!!!!!The amount you are asking for isn't available at the moment sadly ")
						
			if Customer_Choice == 3:
				Fatora_part= open("ITI_Shop_Fatora.txt","w")
				Fatora_part.write("")
				if New_Amount_Flag == 0:
					print("!!!!! You didn't buy anything")
				elif New_Amount_Flag ==1:
					Fatora_part= open("ITI_Shop_Fatora.txt","a+")
					Fatora_part.write("-------------------------------")
					Fatora_part.write("\n")
					Fatora_part.write("        ITI FATORA")
					Fatora_part.write("\n")
					Fatora_part.write("-------------------------------")
					Fatora_part.write("\n")
					Fatora_part.write("Item      Value       Quantity")
					Fatora_part.close()
					for key, value in ITI_Shop_Dict.items():	
						#print(key)
						print("You bought %0.3f kilos of %s so this will cost %0.3f LE" %(float(value[2]), key ,float(float(value[2])*float(value[1]))))
						Fatora_part= open("ITI_Shop_Fatora.txt","a+")
						Fatora_part.write("\n")
						Fatora_part.write("%s | %0.3f LE | %0.3f Kilos" %(key,float(float(value[2])*float(value[1])),float(value[2])))
						Fatora_part.close()
						#sum= 0.0
				print("Therefore the total amount of the bill is %0.3f" %(sum))
				Fatora_part= open("ITI_Shop_Fatora.txt","a+")
				Fatora_part.write("\n")
				Fatora_part.write("\n")
				Fatora_part.write("Total of the order is : %0.3f LE" %(sum))
				Fatora_part.close()
			elif Customer_Choice==0: #return to the previous page
				user =0     
				break
#-----------------End operation based on each mode-------