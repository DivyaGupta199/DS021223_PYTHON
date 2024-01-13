from customers import *
import json


class Admin():
    def __init__(self):
        self.email_id = "Admin123@gmail.com"
        self.password = "Admin@12345"
        try:
            file = open("products.json","w+")
            self.data = json.load(file)
            file.close()
        except Exception as ex:
            self.data = []

    def update_profile(self, password):
        self.password = password

    def Add_products(self):
        product = {}
        product['Name'] = input("Enter the Product Name : ")
        product['Price'] = input("Enter the Price :")
        product['Quantity'] = input("Enter the quantity : ")
        product['Stock'] = input("Enter the stock : ")
        self.data.append(product)
        file = open("Products.json","w")
        json.dump(self.data,file)
        file.close()
        




        
