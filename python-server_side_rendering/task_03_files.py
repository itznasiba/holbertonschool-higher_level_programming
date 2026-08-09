#!/usr/bin/python3
"""Flask application to serve product data from JSON or CSV files."""
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products():
    """Read and parse product data from products.json."""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def read_csv_products():
    """Read and parse product data from products.csv."""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except (FileNotFoundError, ValueError):
        pass
    return products


@app.route('/products')
def products():
    """Display product data based on source and optional id query params."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Load data based on source
    if source == 'json':
        product_list = read_json_products()
    else:
        product_list = read_csv_products()

    # Filter by id if provided
    if product_id is not None:
        try:
            target_id = int(product_id)
            product_list = [p for p in product_list if p.get('id') == target_id]
            if not product_list:
                return render_template('product_display.html',
                                       error="Product not found")
        except ValueError:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=product_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
