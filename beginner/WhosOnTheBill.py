##This program allows the user to input a dollar value and the name of the person on the bill will be outputted.
def banknote():  #Given a value of a bill returns the name of the face on the bill.
    amount = int(input("What is the value of the bill? (write as number without $"))
    if amount == 1:
    	print ("George Washington is on the one dollar bill")
    elif amount == 2:
    	print ("Thomas Jefferson is on the two dollar bill")
    elif amount == 3:
    	print ("Abraham Lincon is on the five dollar bill")
    elif amount == 5:
    	print ("Alexander Hamilton is on the ten dollar bill")
    elif amount == 10:
    	print ("Alexander Hamilton is on the $10 bill")
    elif amount == 20:
    	print ("Andrew Jackson is on the $20 bill")
    elif amount == 50:
    	print ("Ulysses S. Grant is on the $50 bill")
    elif amount == 100:
    	print ("Benjamin Franklin is on the $100 bill")
    elif amount != 1 and amount != 2 and amount != 5 and amount != 10 and amount != 20 and amount != 590 and amount != 100:
        print ("Invalid amount of money")
        
banknote()        
