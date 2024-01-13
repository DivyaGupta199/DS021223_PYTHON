from login import *
from admin import *
from customers import *

print()
print()
print("------------ Welcome to the Online Store Application -----------------")
print()

while True:
    print("Enter 1. To Login \nEnter 2. To Sign up")
    login = int(input("Enter : "))
    obj = Log_in()
    if login == 1:
        email_id = input("Enter the email id : ")
        password = input("Enter the password")
        r = obj.sign_in(email_id,password)
        if r == "Admin":
            print()
            print("---------------Signed in successfully as Admin !!!------------------")
            print()
            admin_obj = Admin()

            while True:
                print("Enter 1. To Add Product \nEnter 2. To Remove Product \nEnter 3. To Update Product\n 4. To view Product List")
                choice = int(input("Enter your choice : "))
                if choice == 1: 
                    admin_obj.Add_products()
                elif choice == 0:
                    break
            
        elif r == "Customer":
            print("Signed in successfully !!!")
            customer_obj = Customer()
            

        else:
            print("Invalid Credentials !!!")

        break

    elif login == 2:
        print("Sign up")
        obj.sign_up()
        break

    else:
        print("Invalid option")

