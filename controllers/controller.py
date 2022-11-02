from flask import render_template
from app import app
from models.shop_list import orders


@app.route('/orders')
def index():
    return render_template('index.html', orders = orders)

@app.route('/orders/<order_num>')
def single_order(order_num):
    return render_template('single_order.html', order = orders[int(order_num)])
        
  
