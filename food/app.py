from flask import Flask, render_template, request, redirect, url_for

import os
import csv
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'goran.cabarkapa1990'
app.config['MAIL_PASSWORD'] = 'kkqqgseklfgxnaaq'

# initialize the Flask-Mail extension
mail = Mail(app)

# mock data for food menu
menu = [
    {"name": "Hamburger", "price": 8.99},
    {"name": "Pizza", "price": 12.99},
    {"name": "Taco", "price": 6.99},
    {"name": "Salad", "price": 9.99}
]

# route for home page
@app.route("/")
def index():
    return render_template("index.html", menu=menu)

# route for placing an order
@app.route('/order', methods=['POST'])
def order():
    # Get the order data from the form
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    item_indices = request.form.getlist('item')
    # Calculate the total price and count the number of items
    total = 0
    num_items = 0
    items = []
    for i in item_indices:
        item = menu[int(i)]
        total += item['price']
        num_items += 1
        items.append(item)

    # Save the order data to a CSV file
    with open('orders.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, email, address, items, total])

    # Render the order confirmation page
    return render_template('order.html', name=name, email=email, address=address, items=items, total=total)

# route for confirming an order
@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    # Get the order data from the form
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    items = request.form.getlist('items[]')
    total = float(request.form['total'])

    # send the confirmation email
    msg = Message('Order Confirmation', sender='goran.cabarkapa1990@gmail.com', recipients=[email])
    msg.body = f'Thank you for your order!\n\nYour order details:\nName: {name}\nAddress: {address}\nItems: {items}\nTotal: {total}'
    mail.send(msg)

    # Render the "confirm" page
    return render_template('confirm.html', name=name, email=email, address=address, items=items, total=total)



if __name__ == "__main__":
    app.run(debug=True)
