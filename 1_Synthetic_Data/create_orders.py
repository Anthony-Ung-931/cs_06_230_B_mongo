import csv
import random
import json

'''
Pseudocode for order generation
'''
class ARGS:
    SAVE_CUSTOMERS = True
    SAVE_PRODUCTS = True

class CONFIG:
    NUM_ORDERS = 100

class Meta:
    SchemaVersion = 1
    DocumentVersion = 1
    Source = 'Typical order placed by customer.'

'''
Global variables
'''
customers = []
products = []
orders = []


class Customer:
    def __init__(self, Name, Email, Phone):
        self.Name = Name
        self.Email = Email
        self.Phone = Phone
    
    def __str__(self):
        return f'{self.Name}' '\n' f'{self.Email}' '\n' f'{self.Phone}' '\n'


class Product:
    def __init__(self, Name, Price, Category, Manufacturer=None):
        self.Name = Name
        self.Price = Price
        self.Category = Category
        self.Manufacturer = Manufacturer


class Order:
    def __init__(self):
        '''
            Logic for order creation is as follows:
            Select a customer at random
            Select 1 or more items at random
            Set the quantity of some items (rare) higher than 1.
        '''
        pass


'''
    This code will read the CSV data from the customer and product CSVs.
    My reading of CSV code from my parallel project is put here.
'''
def read_csvs():
    csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)

    with open(r'customers.csv', 'r') as csvfile:
        for row in csv.DictReader(csvfile, dialect='piper'):
            Name = row['name']
            Email = row['email']
            Phone = row['phone']

            customer = Customer\
                (Name=Name, Email=Email, Phone=Phone)
            
            customers.append(customer)

    with open(r'products.csv', 'r') as csvfile:
        for row in csv.DictReader(csvfile, dialect='piper'):
            Name = row['Name']
            Price = round(float(row['Price']), 2)
            Category = row['Category']
            Manufacturer = row['Manufacturer']

            product = Product\
                (Name=Name, Price=Price, Category=Category, Manufacturer=Manufacturer)
            
            products.append(product)
    
    '''
        No need to print these out anymore.
    '''


'''
    Refer to the schema file for an example of what is needed for an order.
'''
def make_orders():
    for _ in range(CONFIG.NUM_ORDERS):
        order = {}

        # Populate meta from the class Meta
        meta = {
            'schema_version' : Meta.SchemaVersion,
            'document_version' : Meta.DocumentVersion,
            'source' :  Meta.Source
        }

        order['meta'] = meta

        # Populate ContactInfo from a Customer selected at random

        customer = random.choice(customers)

        contact_info = {
            'name' : customer.Name,
            'email' : customer.Email,
            'phone' : customer.Phone
        }

        order['contact_info'] = contact_info

        '''
            TO DO:
            Populate an address
        '''


        # [1] Select products at random
        # [2] Have some mechanism to save duplicates.
        # [3] Store the total, products, and quantities as variables
        # [4] Stick them in the JSON
        order_products = []

        for _ in range(random.randint(1, 8)):
            product = random.choice(products)
            

        print(json.dumps(obj=order, indent=4))

        '''
            Populate OrderInfo as follows:
                Date: Selected at random
                Select products and quantities at random and then derive the total
        '''

        '''
            Populate an array of products
                Make sure the quantity is consistent with what we have for the total
        '''

        '''
            Shipping
                Select a shipper at random
        '''

        pass

    pass

'''
    This will populate 3 separate JSON files from the 3 global arrays.
'''
def build_json():
    print("TO DO: Build all 3 JSON files from the 3 global arrays")


def run():
    read_csvs()
    make_orders()
    build_json()


run()