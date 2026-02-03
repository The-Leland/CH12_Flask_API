from flask import jsonify, request

from db import product_records


def add_product():
    post_data = request.form if request.form else request.json

    if "product_id" not in post_data or "product_name" not in post_data:
        return jsonify({"message": "product_id and product_name are required"}), 400
    
    active_value = post_data.get("active", True)

    product = {}

    product['product_id'] = post_data['product_id']
    product['product_name'] = post_data['product_name']
    product['description'] = post_data['description']
    product['price'] = post_data['price']

    product['active'] = active_value

    product_records.append(product)

    return jsonify({"message": "product added", "result": product}), 201


def get_product_by_id(product_id):
    for product in product_records:

        if product['product_id'] == str(product_id):
            return jsonify({"message": "product found", "result": product}), 200
        
    return jsonify({"message": "product not found"}), 400

def get_all_products():
    return jsonify({"message": "products found", "results": product_records}), 200

def get_active_products():
    active_list = [p for p in product_records if p.get("active") is True]
    return jsonify({"message": "active products", "results": active_list}), 200


def update_product_by_id(product_id):
    post_data = request.form if request.form else request.json

    product = {}

    for record in product_records:
        if record['product_id'] == str(product_id):
            product = record

    if product == {}:
        return jsonify({"message": "product not found"}), 400

    product['product_name'] = post_data.get('product_name', product['product_name'])
    product['description'] = post_data.get('description', product['description'])
    product['price'] = post_data.get('price', product['price'])

    return jsonify({"message": "product updated", "result": product}), 200

def update_product_active(product_id):
    post_data = request.form if request.form else request.json

    if "active" not in post_data:
        return jsonify({"message": "active field required"}), 400
    
    for product in product_records:
        if product['product_id'] == str(product_id):
            product['active'] = post_data['active']
            return jsonify({"message": "active updated", "result": product}), 200
        
    return jsonify({"message": "product not found"}), 400

def delete_product(product_id):
    for product in product_records:
        if product['product_id'] == str(product_id):
            product_records.remove(product)
            return jsonify({"message": "product delete"}), 200
        
    return jsonify({"message": "product not found"}), 400

    