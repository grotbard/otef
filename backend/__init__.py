from flask import Flask

app = Flask(__name__)

# Load your config here, e.g., app.config.from_object('config.DevelopmentConfig')

# Register the blueprint
from backend.facebook_login.routes import facebook_login_bp
app.register_blueprint(facebook_login_bp)

if __name__ == '__main__':
    app.run(debug=True)
