from datetime import datetime
#---------Reading the prices from the prices database------------
Prices_File=open("Pola_Shop_Pricing_Database.txt","r")
#print(Prices_File.read())
counter=1
for i in range(0,3):
	Prices_File_Line = Prices_File.readline()
	if (counter ==1):
		Small_Price= Prices_File_Line[Prices_File_Line.find("small") +6 : Prices_File_Line.rfind("*")]
		counter=counter+1
		#print(Small_Price)
	elif (counter ==2):
		Medium_Price= Prices_File_Line[Prices_File_Line.find("medium") +7 : Prices_File_Line.rfind("*")]
		#print(Medium_Price)
		counter=counter+1
	elif (counter ==3):
		Large_Price= Prices_File_Line[Prices_File_Line.find("large") +6 : Prices_File_Line.rfind("*")]
		#print(Large_Price)
#----------------------------------------------------------------
#----------Giving the customer buying options -------------------
print("------Welcome to pola's asab shop------")
Small_Asab=0  #counter for small asab for each customer
Medium_Asab=0 #counter for medium asab for each customer
Large_Asab=0 #counter for large asab for each customer
Customer_Name=input("---> Please enter your name here : ")
while(1):	
	print("--------------------------------------")
	print("To buy Small asab Enter 1")
	print("To buy Medium asab Enter 2")
	print("To buy Large asab Enter 3")
	print("To see your cart Enter 4")
	print("To see the cost of your cart Enter 5")
	print("To exit asab shop Enter 0")
	print("--------------------------------------")
	Customer_Choice = int(input("Please enter the number corresponding to your choice : "))
	Customer_Choice_List=[0,1,2,3,4,5]
	while (Customer_Choice not in Customer_Choice_List):
		print("!!!!!Invalid Choice")
		print("To buy Small asab Enter 1")
		print("To buy Medium asab Enter 2")
		print("To buy Large asab Enter 3")
		print("To exit asab shop Enter 0")
		Customer_Choice = int(input("Please enter the number corresponding to your choice : "))

	if (Customer_Choice == 1):
		Small_Asab=Small_Asab+1
		Selling_File = open("Pola_Shop_Selling_DataBase.txt","a+")
		Selling_File.write("Custommer -%s- bought a *Small* asab " %(Customer_Name) + " At " +str(datetime.now()))
		Selling_File.write("\n")
		Selling_File.close()
		
	elif (Customer_Choice == 2):
		#print("Medium")
		Medium_Asab=Medium_Asab+1
		Selling_File = open("Pola_Shop_Selling_DataBase.txt","a+")
		Selling_File.write("Custommer -%s- bought a *Medium* asab " %(Customer_Name) + " At " +str(datetime.now()))
		Selling_File.write("\n")
		Selling_File.close()
	
	elif (Customer_Choice == 3):
		Large_Asab=Large_Asab+1
		Selling_File = open("Pola_Shop_Selling_DataBase.txt","a+")
		Selling_File.write("Custommer -%s- bought a *Large* asab " %(Customer_Name) + " At " +str(datetime.now()))
		Selling_File.write("\n")
		Selling_File.close()
	
	elif (Customer_Choice == 4):
		if (Small_Asab != 0):
			print("------You ordered %d of Small asab------"%(Small_Asab))
		if (Medium_Asab != 0):
			print("------You ordered %d of medium asab-----"%(Medium_Asab))
		if (Large_Asab != 0):
			print("------You ordered %d of Large asab------"%(Large_Asab))
	
	
	elif (Customer_Choice == 5):
		Total_Cost = 0
		if (Small_Asab != 0):
			Total_Small_Asab_Price = Small_Asab * int(Small_Price)
			print("The total cost of Small asab is %d which comes from : %d small asab * %s LE" %(Total_Small_Asab_Price,Small_Asab,Small_Price))
		if (Medium_Asab != 0):
			Total_Medium_Asab_Price =Medium_Asab * int(Medium_Price)
			print("The total cost of Medium asab is %d which comes from : %d Medium asab * %s LE" %(Total_Medium_Asab_Price,Medium_Asab,Medium_Price))
		if (Large_Asab != 0):
			Total_Large_Asab_Price = Large_Asab * int(Large_Price)
			print("The total cost of Large asab is %d which comes from : %d Large asab * %s Le"%(Total_Large_Asab_Price,Large_Asab,Large_Price))
		Total_cost = Total_Large_Asab_Price + Total_Medium_Asab_Price + Total_Small_Asab_Price
		print("The total cost of your cart is : %d" %(Total_cost))
		
	elif (Customer_Choice == 0):
		break
