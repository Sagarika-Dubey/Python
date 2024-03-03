bill=0
total_bill=[]
total=0
discount=0.2
dis_sub=0
items_pur=[]
rice=wheat=dal=potatoes=onion=tomato=soya=carrot=100
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
        items_pur.append("Rice")
        quant=int(input("Enter how many kgs do you want-"))
        bill=40*quant
        total_bill.append(bill)
        print("You will have to pay-",bill,"Rs.")
        rice=100-quant
    elif(choice=="2"):
        items_pur.append("Wheat")
        quant=int(input("Enter how many kgs do you want-"))
        bill=50*quant
        total_bill.append(bill)
        print("You will have to pay-",bill,"Rs.")
        wheat=100-quant
    elif(choice=="3"):
        items_pur.append("Dal")
        quant=int(input("Enter how many kgs do you want-"))
        bill=30*quant
        total_bill.append(bill)
        print("You will have to pay-",bill,"Rs.")
        dal=100-quant
    elif(choice=="4"):
        items_pur.append("Potatoes")
        quant=int(input("Enter how many kgs do you want-"))
        bill=25*quant
        total_bill.append(bill)
        print("You will have to pay-",bill,"Rs.")
        potatoes=100-quant
    elif(choice=="5"):
        items_pur.append("Onion")
        quant=int(input("Enter how many kgs do you want-"))
        bill=35*quant
        total_bill.append(bill)
        print("You will have to pay-",bill,"Rs.")
        onion=100-quant
    elif(choice=="6"):
        items_pur.append("Tomato")
        quant=int(input("Enter how many kgs do you want-"))
        bill=30*quant
        total_bill.append(bill)
        print("You will have to pay-",bill,"Rs.")
        tomato=100-quant
    elif(choice=="7"):
        items_pur.append("Soya Chunks")
        quant=int(input("Enter how many packets do you want-"))
        bill=25*quant
        total_bill.append(bill)
        print("You will have to pay-",bill,"Rs.")
        soya=100-quant
    elif(choice=="8"):
        items_pur.append("Carrot")
        quant=int(input("Enter how many kgs do you want-"))
        bill=40*quant
        total_bill.append(bill)
        print("You will have to pay-",bill,"Rs.")
        carrot=100-quant
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

