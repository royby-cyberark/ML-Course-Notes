from functools import reduce

CUSTOMERS_FILE = 'cust.csv'
ORDERS_FILE = 'orders.csv'

def get_customer_id(name: str) -> str:
    with open(CUSTOMERS_FILE, 'r') as file:
        cust_lines = file.readlines()

    customer_details = [details.split(',') for details in cust_lines if details.split(',')[1] == name]
    if customer_details:
        return customer_details[0][0]
    else: 
        raise Exception("Customer not found")


def get_cusomer_orders(customer_id: int):
    with open(ORDERS_FILE, 'r') as file:
        order_lines = file.readlines()
    
    return [order_line.split(',') for order_line in order_lines if order_line.split(',')[1] == customer_id]

def calc_sum(list_of_orders):
    return reduce(lambda i, order: i + int(order[3]), list_of_orders, 0)

while True:
    try:
        customer_name = input('Enter customer name: ')
        customer_id = get_customer_id(customer_name)
        print(f'customer id: {customer_id}')
        customer_orders = get_cusomer_orders(customer_id)
        print(calc_sum(customer_orders))

    except Exception as ex:
        print(ex) 
    