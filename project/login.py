from admin import *
import json

class Log_in():
    def __init__(self):
        try:
            file = open("customers_info.json","r")
            self.customers = json.load(file)
            file.close()

        except:
            self.customers = []

    def sign_in(self,email_id, password):
        obj = Admin()
        if email_id == obj.email_id and password == obj.password:
            return "Admin"
        
        else:
            for d in self.customers:
                if email_id in d.values() and password in d.values():
                    return "Customer"
            
            return "Invalid"

    def sign_up(self):
        data = {}
        data['Name'] = input("Enter your name : ")
        data['Phone_number'] = input("Enter your phone_number : ")
        data['email'] = input("Enter your email id : ")
        data['password'] = input("Enter the password : ")
        data['Address'] = input("Enter the Address : ")
        data['orders'] = []
        data['wishlist'] = []

        self.customers.append(data)

        file = open("customers_info.json","w")
        json.dump(self.customers,file)
        file.close()
        