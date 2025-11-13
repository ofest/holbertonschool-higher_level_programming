from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    return render_template('items.html')


@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    data = []
    error = None

    if source == 'json':
        try:
            with open('products.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            error = "Error reading JSON file"
            return render_template('product_display.html', error=error)

    elif source == 'csv':
        try:
            with open('products.csv', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row["id"] = int(row["id"])
                    row["price"] = float(row["price"])
                    data.append(row)
        except Exception:
            error = "Error reading CSV file"
            return render_template('product_display.html', error=error)

    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            query = "SELECT * FROM Products"
            params = ()

            if product_id:
                query += " WHERE id = ?"
                params = (product_id,)

            cursor.execute(query, params)
            rows = cursor.fetchall()
            conn.close()


            for row in rows:
                data.append({
                    "id": row["id"],
                    "name": row["name"],
                    "category": row["category"],
                    "price": row["price"]
                })

            if product_id and not data:
                error = "Product not found"

        except Exception as e:
            error = "Database error: " + str(e)
            return render_template('product_display.html', error=error)


    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)


    if product_id and source != 'sql':
        try:
            product_id = int(product_id)
            data = [item for item in data if item['id'] == product_id]
            if not data:
                error = "Product not found"
        except ValueError:
            error = "Invalid product ID"
            data = []

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
