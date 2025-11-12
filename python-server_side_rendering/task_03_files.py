from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)

def read_csv(file_path):
    products = []
    with open(file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert id to int and price to float
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', None)

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")


    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in data if p['id'] == product_id]
            if not filtered:
                return render_template('product_display.html', error="Product not found")
            data = filtered
        except ValueError:
            return render_template('product_display.html', error="Invalid id")

    return render_template('product_display.html', products=data)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

