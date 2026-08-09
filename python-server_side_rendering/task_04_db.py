#!/usr/bin/python3
"""Flask application to serve product data from JSON, CSV, or SQLite database."""
import csv
import json
import sqlite3
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


def read_sql_products(product_id=None):
    """Fetch product data from SQLite database with optional filtering by id."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        if product_id is not None:
            cursor.execute(
                "SELECT id, name, category, price FROM Products WHERE id = ?",
                (product_id,)
            )
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")

        rows = cursor.fetchall()
        conn.close()

        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        return products
    except sqlite3.Error:
        return None


@app.route('/products')
def products():
    """Display product data based on source (json/csv/sql) and optional id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validate source query parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # Fetch data based on source
    if source == 'json':
        product_list = read_json_products()
    elif source == 'csv':
        product_list = read_csv_products()
    elif source == 'sql':
        if product_id is not None:
            try:
                target_id = int(product_id)
            except ValueError:
                return render_template('product_display.html',
                                       error="Product not found")

            product_list = read_sql_products(target_id)
            if product_list is None:
                return render_template('product_display.html',
                                       error="Database error")
            if not product_list:
                return render_template('product_display.html',
                                       error="Product not found")
            return render_template('product_display.html', products=product_list)

        product_list = read_sql_products()
        if product_list is None:
            return render_template('product_display.html', error="Database error")
        return render_template('product_display.html', products=product_list)

    # Filter JSON and CSV data by id if provided
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
    app.run(host='0.0.0.0', port=5000, debug=True)
