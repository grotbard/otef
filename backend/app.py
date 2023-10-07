from flask import Flask, Blueprint, request, jsonify
import requests


app = Flask(__name__)

# Load your config here, e.g., app.config.from_object('config.DevelopmentConfig')

# Define the blueprint
facebook_login_bp = Blueprint('facebook_login', __name__)

# Define users (for testing purposes)
users = {
    'your_facebook_access_token': {'name': 'John Doe', 'email': 'john.doe@example.com'},
}


# Route for Facebook login
@facebook_login_bp.route('/facebook_login', methods=['POST'])
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


# Function to validate Facebook access token (replace with your actual logic)
def validate_facebook_access_token(access_token):
    # Make a request to the Facebook Graph API to validate the token
    url = f'https://graph.facebook.com/debug_token'
    params = {
        'input_token': access_token,
        'access_token': f'345341791279729|c4eac77e172ca98ed349ecbb852eebcd'  # Replace with your actual App ID and App Secret
    }

    response = requests.get(url, params=params)
    data = response.json()

    if 'data' in data and data['data']['is_valid']:
        return True
    else:
        return False


# Register the blueprint
app.register_blueprint(facebook_login_bp)

if __name__ == '__main__':
    app.run(debug=True)
