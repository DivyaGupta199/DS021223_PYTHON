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
                print("Enter 1. To Add Product \nEnter 2. To Remove Product \nEnter 3. To Update Product\nEnter 4. To view Product List\nEnter 0. To Exit")
                choice = int(input("Enter your choice : "))
                if choice == 1: 
                    admin_obj.Add_products()

                elif choice == 2:
                    product = input("Enter the Name of the product you would like to remove : ")
                    admin_obj.remove_product(product)

                elif choice == 3:
                    name = input("Enter the name of the product to update : ")
                    parameter = input("Which parameter you would like to change : ")
                    new_value = input("What is the updated value for the above mentioned parameter : ")
                    admin_obj.update_product(name, parameter, new_value)

                elif choice == 4:
                    admin_obj.display_product_list()

                elif choice == 0:
                    break

                else:
                    print("Invalid choice")
            
        elif r == "Customer":
            print("Signed in successfully !!!")
            customer_obj = Customer()
            while True:
                print("Enter 1. To View Product List \nEnter 2. To Add Products to Wishlist \nEnter 3. Order Products \nEnter 4. Update Profile \nEnter 5. To view Order History \nEnter 0. To Exit")
                choice = int(input("Enter your choice : "))
                if choice == 1:
                    customer_obj.display_product()

                elif choice == 2:
                    product = input("Enter the Product name : ")
                    customer_obj.Add_product_to_whislist(email_id, product)

                elif choice == 3:
                    customer_obj.order_product(email_id)

                elif choice == 4:
                    parameter = input("Enter the parameter you want to update : ")
                    new_data = input("Enter the updated value")
                    customer_obj.update_profile(email_id,parameter,new_data)

                elif choice == 5:
                    customer_obj.view_order_history(email_id)

                elif choice == 0:
                    break

                else:
                    print("Invalid choice!!!")


            

        else:
            print("Invalid Credentials !!!")

        break

    elif login == 2:
        print("Sign up")
        obj.sign_up()
        break

    else:
        print("Invalid option")

