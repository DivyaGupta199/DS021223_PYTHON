import json
import pandas as pd
import datetime as dt

class Customer:
    def __init__(self):
            file = open("products.json","r")
            self.data = json.load(file)
            file.close()

            file = open("customers_info.json","r")
            self.customer = json.load(file)
            file.close()

    def display_product(self):
        df = pd.DataFrame(self.data)
        print(df)

    def Add_product_to_whislist(self,email,product):
        for i in self.data:
            if product in i.values():
                status = True
                for c in self.customer:
                    if email in c.values():
                        lst = c['wishlist']
                        lst.append(product)
                        c['wishlist'] = lst
                        break

                file = open("customers_info.json","w")
                json.dump(self.customer,file)
                file.close()
                break
            
            else:
                status = False

        if status:
            print("Product found")
        else:
            print("Product not found!!!")
        
    def order_product(self,email):
        order_products = []
        while True:
            product = input("Enter the name of the product")
            for i in self.data:
                if product in i.values():
                    status = True
                    order_products.append(product)
                    break

                else:
                    status = False

            if status == False:
                print("Product not found")

            choice = input("Enter 'Y' to order more products or any other Key to exit")
            if choice != 'Y':
                break

            date = dt.datetime.now()
            dict_order = {}
            dict_order[str(date)] = order_products

            for c in self.customer:
                if email in c.values():
                    lst = c['orders']
                    lst.append(dict_order)
                    c['orders'] = lst

                file = open("customers_info.json","w")
                json.dump(self.customer,file)
                file.close()
                print("Order made successfully!!! It will be Delivered to your Address shortly!!!")
                break
                
    def update_profile(self,email,parameter,new_data):
        for i in self.customer:
            if email in i.values():
                if parameter in i.keys():
                    i[parameter] = new_data
                    status = True
                    break
            
                else:
                    status = False

        if status == False:
            print(f"{parameter} not a valid parameter to update!!!")

        file = open("customers_info.json","w")
        json.dump(self.customer, file)
        file.close()
        print("Profile updated successfully!!!")
        
    def view_order_history(self,email):
        for i in self.customer:
            if email in i.values():
                lst = i['orders']
                df = pd.DataFrame(lst)
                print(df)            

        