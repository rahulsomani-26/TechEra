import random

class Customer:
    """Customer Class that creates a unique customer"""
    customer_id = 0 

    def __init__(self,cust_name,cust_address,cust_email,product,price,quantity):
        
        self.customer_id = Customer.customer_id
        Customer.customer_id = Customer.customer_id+ 1
        self.cust_name = cust_name
        self.cust_address = cust_address
        self.cust_email = cust_email
        self.product = product
        self.price = price
        self.quantity = quantity
        print('Customer data initialized')


    def update_record(self):
        """Should be a database where a table should be created"""

        
          





    def __repr__(self):
        return 'Customer(id={},name={})'.format(self.customer_id, self.cust_name)

    
if __name__ == '__main__':
    customer = Customer('rahul','204,Tulip Park,Marol Military Road,Andheri(E)','customer@yours.com','Arduino',19000,1)
    print(customer)
    print(repr(customer))

