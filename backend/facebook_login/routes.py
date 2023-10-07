from flask import request, jsonify
from backend import app
import requests

users = {
    'your_facebook_access_token': {'name': 'John Doe', 'email': 'john.doe@example.com'},
}


@app.route('/facebook_login', methods=['POST'])
def facebook_login():
    try:
        data = request.get_json()
        access_token = data.get('accessToken')

        if validate_facebook_access_token(access_token):
            user_data = users[access_token]
            return jsonify({'success': True, 'userData': user_data})
        else:
            return jsonify({'success': False, 'error': 'Invalid token'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

def validate_facebook_access_token(access_token):
    url = f"https://graph.facebook.com/debug_token"
    params = {
        "input_token": access_token,
        "access_token": "345341791279729|c4eac77e172ca98ed349ecbb852eebcd"  # Replace with your app ID and secret
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'data' in data and data['data']['is_valid']:
        return True
    else:
        return False

