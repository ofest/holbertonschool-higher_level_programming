from flask import Flask, render_template, request
import json
import csv


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


from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

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

    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)
    
    if product_id:
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
