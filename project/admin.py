from customers import *
import json
import pandas as pd


class Admin():
    def __init__(self):
        self.email_id = "Admin123@gmail.com"
        self.password = "Admin@12345"
        try:
            file = open("products.json","r")
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
        
    def update_product(self,product,parameter,new_value):
        for i in self.data:
            if product in i.values():
                i[parameter] = new_value
                status = True
                break
            
            else:
                status = False

        if status == True:
            print("changes updated")
            print(self.data)


        file = open("products.json","w")
        json.dump(self.data, file)
        file.close()
        

    def remove_product(self,product):
        for i in self.data:
            if product in i.values():
                self.data.remove(i)
                status = True
                break
            
            else:
                status = False
        
        if status:
            print("Product removed from the product list successfully!!!")
            file = open("products.json","w")
            json.dump(self.data,file)
            file.close()
        else:
            print("Product not found!!!")

    def display_product_list(self):
        df = pd.DataFrame(self.data)
        print(df)




        
