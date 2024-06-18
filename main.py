import os
import yaml
from flask import *
from all_functions import *
import json


app = Flask(__name__)

@app.route('/')
def main():
    items = get_iam_categories()
    role_data = get_roles_data()
    return render_template("index.html", items=items, role_data=role_data)

@app.route('/all-roles')
def all_roles():
    items = get_iam_categories()
    role_data = get_roles_data()
    return render_template("all_roles.html", items=items, role_data=role_data)

@app.route('/search')
def search():
    items = get_iam_categories()
    return render_template('search_page.html', items=items)

@app.route('/iam-classes')
def iam_classes():
    source = request.args.get('parameter')
    items = get_iam_categories()
    specific_items = get_specific_roles(source)
    print(specific_items)
    return render_template("iam-classes.html", specific_items=specific_items, items=items)

@app.route('/tsid', methods=['GET'])
def tsid():
    data = get_tsid()
    return jsonify(data)

@app.route('/eu-eea', methods=['GET'])
def eueea():
    country_code = get_country_codes()
    return is_eea(country_code)

@app.route('/machine_pricing', methods=['GET'])
def machine_pricing():
    with open('pricing.yml', 'r') as file:
        pricing_data = yaml.safe_load(file)
    return render_template('machine_pricing.html', pricing_data=pricing_data)

if __name__ == '__main__':
    app.run(debug=False)
