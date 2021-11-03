class CustomerOrder:
    """Keep tracks of the customer order"""
    def __init__(self,obj):
        self.obj = obj 

    def __str__(self):
        return 'CustomerOrder'

    def __repr__(self):
        return f'CustomerOrder({self.obj})'

        
