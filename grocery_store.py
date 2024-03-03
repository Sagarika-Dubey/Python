bill=0
total_bill=[]
total=0
discount=0.2
dis_sub=0
items_pur=[]
rice=50
wheat=50
dal=55
potatoes=onion=tomato=10
soya=25
carrot=15
print("Hey Customer! Welcome to our grocery store:)")
print("Grocery menu:")
print("1.Rice -> 40Rs. per kg\n"
          "2.Wheat -> 50Rs. per kg\n"
          "3.Dal -> 30Rs. per kg\n"
          "4.Potatoes -> 25Rs. per kg\n"
          "5.Onion -> 35Rs. per kg\n"
          "6.Tomato -> 30Rs. per kg \n"
          "7.Soya Chunks -> 25Rs.per Packet(250 gram)\n"
          "8.Carrot -> 40Rs. per kg")
    
ans="yes"
while (ans=="yes"):
    choice=input("\nenter ur choice:")

    if(choice=="1"):
        quant=int(input("Enter how many kgs do you want-"))
        rice=50-quant
        if rice>0:
            items_pur.append("Rice")
            bill=40*quant
            total_bill.append(bill)
            print("You will have to pay-",bill,"Rs.")
        else:
            print("Sorry insufficient stock avalibility \nCurrent stock=",rice)            
        
    elif(choice=="2"):        
        quant=int(input("Enter how many kgs do you want-"))
        wheat=50-quant
        if wheat>0:
            items_pur.append("Wheat")
            bill=50*quant
            total_bill.append(bill)
            print("You will have to pay-",bill,"Rs.")
        else:
            print("Sorry insufficient stock avalibility \nCurrent stock=",wheat)
        
    elif(choice=="3"):        
        quant=int(input("Enter how many kgs do you want-"))
        dal=55-quant
        if dal>0:
            items_pur.append("Dal")
            bill=30*quant
            total_bill.append(bill)
            print("You will have to pay-",bill,"Rs.")        
        else:
            print("Sorry insufficient stock avalibility \nCurrent stock=",dal)
    elif(choice=="4"):        
        quant=int(input("Enter how many kgs do you want-"))
        potatoes=10-quant
        if potatoes>0:
            items_pur.append("Potatoes")
            bill=25*quant
            total_bill.append(bill)
            print("You will have to pay-",bill,"Rs.")        
        else:
            print("Sorry insufficient stock avalibility \nCurrent stock=",potatoes)
            
    elif(choice=="5"):        
        quant=int(input("Enter how many kgs do you want-"))
        onion=10-quant
        if onion>0:
            items_pur.append("Onion")
            bill=35*quant
            total_bill.append(bill)
            print("You will have to pay-",bill,"Rs.")        
        else:
            print("Sorry insufficient stock avalibility \nCurrent stock=",onion)
    elif(choice=="6"):        
        quant=int(input("Enter how many kgs do you want-"))
        tomato=10-quant
        if tomato>0:
            items_pur.append("Tomato")
            bill=30*quant
            total_bill.append(bill)
            print("You will have to pay-",bill,"Rs.")        
        else:
            print("Sorry insufficient stock avalibility \nCurrent stock=",tomato)
    elif(choice=="7"):        
        quant=int(input("Enter how many packets do you want-"))
        soya=25-quant
        if soya>0:
            items_pur.append("Soya Chunks")
            bill=25*quant
            total_bill.append(bill)
            print("You will have to pay-",bill,"Rs.")        
        else:
            print("Sorry insufficient stock avalibility \nCurrent stock=",soya)
    elif(choice=="8"):        
        quant=int(input("Enter how many kgs do you want-"))
        carrot=15-quant
        if carrot>0:
            items_pur.append("Carrot")
            bill=40*quant
            total_bill.append(bill)
            print("You will have to pay-",bill,"Rs.")        
        else:
            print("Sorry insufficient stock avalibility \nCurrent stock=",carrot)
    else:
        print("Please enter a valid choice")

    ans=input("Do you want to still continue(yes/no)?")
    if (ans=="yes"):
        continue
    else:
        print("\nBILL-")
        for i in range(len(items_pur)):
            print(items_pur[i])
        for i in range(len(total_bill)):
               total=total+total_bill[i]
        print("\nYour Amount-",total)
        dis_sub=total*discount
        total=total-dis_sub
        print("We provide 20% Discount on every purchase our customer makes")
        print("Your Total Bill-",total)
        break

decision=input("Do you want to see the stocks avalibale(yes/no)?")
if (decision=="yes"):
    print("Rice=",rice,"\nWheat=",wheat,"\nDal=",dal,"\nPotatoe=",potatoes,"\nOnion=",onion,"\nTomato=",tomato,"\nSoya Chunks=",soya,"\nCarrot=",carrot)
else:
    print("Okay! Thank you")

print("Thanks for shopping with us❤ \nDo visit the store again:)")

