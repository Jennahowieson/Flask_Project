from models.order import *
from datetime import datetime



order1 = Order("Customer1", datetime.now().strftime('%d-%m-%y %H:%M'), 1, "Book of Pizza", 0)
order2 = Order("Customer2", datetime.now().strftime('%d-%m-%y %H:%M'), 2, "Dictionary", 1)
orders = [order1, order2]