import os
from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

API_URL_FIND_BY_USER = "https://yayawallet.com/api/en/transaction/find-by-user"
API_URL_SEARCH = "https://yayawallet.com/api/en/transaction/search"
API_KEY = os.getenv('key-test_493e9539-3765-493a-864d-1082e2636168') 
API_SECRET = os.getenv('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcGlfa2V5Ijoia2V5LXRlc3RfNDkzZTk1MzktMzc2NS00OTNhLTg2NGQtMTA4MmUyNjM2MTY4Iiwic2VjcmV0IjoiMDUyOTNjMGU1MDlhOWE4ODRiMDVhMWYwZjkzYjdiNjMzMmE1NDUwMSJ9.is7GgbMLZ_ZUT1He9DG1dtEs5CxfpkVlCco0Xo6mHQY ') 

headers = {
    'Authorization': f'Bearer {API_KEY}:{API_SECRET}',
    'Content-Type': 'application/json'
}

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/transactions', methods=['GET'])
def get_transactions():
    page = request.args.get('p', 1)
    query = request.args.get('query', '')
    params = {'page': page}
   
    if query:
        response = requests.post(
            API_URL_SEARCH,
            headers=headers,
            json={'query': query}
        )
    else:
        response = requests.get(
            API_URL_FIND_BY_USER,
            headers=headers,
            params=params
        )
   
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Unable to fetch transactions'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)