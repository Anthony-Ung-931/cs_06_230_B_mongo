'''
Pseudocode for order generation
'''
class ARGS:
    SAVE_CUSTOMERS = True
    SAVE_PRODUCTS = True


'''
Global variables
'''
customers = []
products = []
orders = []


class Customer:
    def __init__(self, **kwargs):
        pass


class Product:
    def __init__(self, **kwargs):
        pass


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
    pass
'''
        csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)
        
        with open('Products1.txt', 'r') as csvfile:
            count = 0
            
            for row in csv.DictReader(csvfile, dialect='piper'):
                sku = int(row.get('SKU'))
                product_name = row.get('Product Name')
                product_type = row.get('itemType')
                manufacturer = row.get('Manufacturer')
                base_price = row.get('BasePrice')

                price = float(Decimal(base_price.strip('$')))
                price = round(price * params.group.price_multiplier, 2)

                current_product = Product(\
                    p_name = product_name, \
                    p_type = product_type, \
                    sku = sku, 
                    price = price
                )
                
                db.execute_sql_values( \
                        sql='insert into products values (?, ?, ?, ?, ?)',\
                        values=(sku, product_name, product_type, manufacturer, base_price))

                match product_type:
                    case 'Milk':
                        Inventory.products['milk'].append(current_product)
                    case 'Cereal':
                        Inventory.products['cereal'].append(current_product)
                    case 'Baby Food':
                        Inventory.products['baby food'].append(current_product)
                    case 'Diapers':
                        Inventory.products['diapers'].append(current_product)
                    case 'Bread':
                        Inventory.products['bread'].append(current_product)
                    case 'Peanut Butter':
                        Inventory.products['peanut butter'].append(current_product)
                    case 'Jelly/Jam':
                        Inventory.products['jelly jam'].append(current_product)
                    case _:
                        Inventory.products['other'].append(current_product)
                
                count += 1
                if count % 10000 == 0:
                    db.commit()
                    print(f"Committed {count} products")
                
            db.commit()
            print(f"Committed {count} products")
'''



'''
    This will populate 3 separate JSON files from 3 separate arrays.
'''
def build_json():
    pass


def run():
    pass


run()