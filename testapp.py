import os
import requests
from flask import Flask, redirect, url_for, session, request, render_template
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get OAuth credentials from .env file
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
AUTHORIZATION_BASE_URL = os.getenv('AUTHORIZATION_BASE_URL')
TOKEN_URL = os.getenv('TOKEN_URL')
USER_API_URL = os.getenv('USER_API_URL')
SECRET_KEY = os.getenv('SECRET_KEY')


# Scopes: Request access to user emails and private repositories
scope = "read:user user:email repo"

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Replace with a secure random key

# Initialize OAuth2 session
oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)

@app.route('/')
def index():
    """Homepage with login link"""
    if 'oauth_token' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in

    user_info = get_user_info()
    return render_template('index.html', user_info=user_info)

@app.route('/login')
def login():
    oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI, scope=scope)
    authorization_url, state = oauth.authorization_url(AUTHORIZATION_BASE_URL)
    session['oauth_state'] = state
    return redirect(authorization_url)


@app.route('/callback')
def callback():
    """Callback after GitHub authentication"""
    oauth = OAuth2Session(CLIENT_ID, state=session['oauth_state'], redirect_uri=REDIRECT_URI)
    token = oauth.fetch_token(TOKEN_URL, client_secret=CLIENT_SECRET, authorization_response=request.url)

    # Store the access token in the session
    session['oauth_token'] = token

    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    """Clear the session and log the user out"""
    session.clear()  # Clear all session data
    return redirect(url_for('login'))  # Redirect to the login page

def get_user_info():
    """Get the user's GitHub profile, repositories, and emails"""
    oauth = OAuth2Session(CLIENT_ID, token=session['oauth_token'])

    # Get user info (e.g., username, bio, and avatar)
    user_info = oauth.get(USER_API_URL).json()

    # Get the user's repositories
    user_repos_url = "https://api.github.com/user/repos"
    repos = oauth.get(user_repos_url).json()

    # Get the user's emails
    user_emails_url = "https://api.github.com/user/emails"
    emails = oauth.get(user_emails_url).json()

    # Return the user data
    return {
        'username': user_info['login'],
        'bio': user_info.get('bio', 'No bio available'),
        'avatar_url': user_info['avatar_url'],
        'repos': repos,
        'emails': emails  # Include emails in the returned data
    }


if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'), debug=True)

