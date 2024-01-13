from admin import *

class Log_in():
    def __init__(self):
        pass

    def sign_in(self,email_id, password):
        obj = Admin()
        if email_id == obj.email_id and password == obj.password:
            return "Admin"
        
        else:
            file = open("customer_info.txt","r")
            data = file.readlines()
            file.close()
            for d in data:
                if email_id in d and password in d:
                    return "Customer"
            
            return "Invalid"

    def sign_up(self):
        name = input("Enter your name : ")
        phone_number = input("Enter your phone_number : ")
        email = input("Enter your email id : ")
        password = input("Enter the password : ")
        Address = input("Enter the Address : ")

        file = open("customer_info.txt","a")
        file.write("\n")
        data = f"{name} {phone_number} {email} {password} {Address}"
        file.write(data)
        file.close()