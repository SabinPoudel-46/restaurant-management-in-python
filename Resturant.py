import random
from fpdf import FPDF
def menu():
    global bill_amount,name
    try:
        while True:
            choice_menu=int(input("1.Nepali Cuisine 2.Indian Cuisine 3.Exit:"))
            if choice_menu==1:
                print('''1.Dal Bhat-->200\n2.Momo-->90\n3.Gundruk,Dhido-->400\n4.Sel Roti-->40''')
                choice_nepali=int(input())
                if choice_nepali==1:
                    bill_amount=bill_amount+200
                    f=open("Billamount.txt","a")
                    f.write("Dal Bhat-->Rs200\n")
                    f.close()
                elif choice_nepali==2:
                    bill_amount=bill_amount+90
                    f=open("Billamount.txt","a")
                    f.write("Momo-->Rs90\n")
                    f.close()
                elif choice_nepali==3:
                    bill_amount=bill_amount+400
                    f=open("Billamount.txt","a")
                    f.write("Ghundruk,Dhido-->Rs400\n")
                    f.close()
                elif choice_nepali==4:
                    bill_amount=bill_amount+40
                    f=open("Billamount.txt","a")
                    f.write("Sel Roti-->40\n")
                    f.close()
                else:
                    print("Enter the valid Dish")
            elif choice_menu==2:
                print('''1.Palak Paneer-->Rs170\n2.Chana Masala-->Rs60\n3.Fish Curry-->Rs500''')
                choice_indian=int(input())
                if choice_indian==1:
                    bill_amount=bill_amount+170
                    f=open("Billamount.txt","a")
                    f.write("Palak Paneer-->Rs170\n")
                    f.close()
                elif choice_indian==2:
                    bill_amount=bill_amount+60
                    f=open("Billamount.txt","a")
                    f.write("Chana Masala-->Rs60\n")
                    f.close()
                elif choice_indian==3:
                    bill_amount=bill_amount+500
                    f=open("Billamount.txt","a")
                    f.write("Fish Curry-->Rs500\n")
                    f.close()
                else:
                    print("Enter Valid choice")  
            elif choice_menu==3:
                break
    except:
        print("An Error Occured")
def bill():
    global name
    bill_no=random.randint(1,10)
    bill_no=str(bill_no)
    bill_no="MER"+bill_no
    global bill_amount
    f=open("Billamount.txt","a")
    f.write("""UniqueID for this order is {}\n{}'s final Bill amount is {}\nThanks for using our service""".format(bill_no,name,bill_amount))
    f.close()
    print("Your bill is ready to print")
def display():
    f=open("Billamount.txt","r")
    content=f.readlines()
    for i in content:
        print(i)
def pdf():
    PDF=FPDF()
    PDF.add_page()  
    PDF.set_font("Arial",size=21)
    f=open("Billamount.txt","r")
    for i in f:
        PDF.cell(200,10,txt=i,ln=3,align='C')
    PDF.output("Bill.pdf")
    print("Pdf file Successfully Generated")
def search():
    bill_no=int(input("Enter the bill number: "))
    f=open("Billamount.txt","r")
    content=f.readlines()
    # if content[-3].find(bill_no)==True:
    #     print("Your order is placed\n")
    # else:
    #     print("Your Order is not placed")
    print(content)

#-----RESTURANT Billing SYSTEM--------#

bill_amount=0
project="Restaurant Billing System"
print(project.center(40,"*"))
name=input("Enter Your Name: ")
try:
    while True:
        print("1.Menu 2.Generate Bill 3.Search Bill 4.Display Bill 5.Generate Pdf file 6.Exit")
        choice=int(input("Enter Your Choice: "))
        if choice==1:
            menu()
        elif choice==2:
            bill()
        elif choice==3:
            search()
        elif choice==4:
            display()
        elif choice==5:
            pdf()
        elif choice==6:
            print("Thanks for using our Service")
            break
except:
    print("An Error Occured")
finally:
    print("Have a Good Day {}\n Thanks for using our service".format(name))