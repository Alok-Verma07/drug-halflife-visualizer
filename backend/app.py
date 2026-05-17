from flask import Flask, request, jsonify
from flask_cors import CORS
from database import init_db, get_all_drugs, get_drug, get_drugs_by_category

app = Flask(__name__)
CORS(app)

# Initialize DB when server starts
init_db()

@app.route('/api/drugs')
def get_drugs():
    drugs = get_all_drugs()
    return jsonify(drugs)

@app.route('/api/drug')
def get_single_drug():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'No drug name provided'}), 400
    drug = get_drug(name)
    if drug is None:
        return jsonify({'error': 'Drug not found'}), 404
    return jsonify(drug)

@app.route('/api/drugs/category')
def get_by_category():
    category = request.args.get('name')
    if not category:
        return jsonify({'error': 'No category provided'}), 400
    drugs = get_drugs_by_category(category)
    return jsonify(drugs)

if __name__ == '__main__':
    app.run(debug=True)