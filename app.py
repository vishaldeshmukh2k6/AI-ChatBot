from flask import Flask, render_template, request, session, redirect, url_for
from responses import get_bot_response
from datetime import timedelta
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.permanent_session_lifetime = timedelta(days=7)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if 'chat' not in session:
        session['chat'] = []

    if request.method == 'POST':
        user_input = request.form['user_input']
        bot_reply = get_bot_response(user_input)
        session['chat'].append({'user': user_input, 'bot': bot_reply})
        session.modified = True

    return render_template('chatbot.html', chat=session['chat'])

@app.route('/reset')
def reset():
    session.pop('chat', None)
    return redirect(url_for('chatbot'))

@app.route('/github', methods=['GET', 'POST'])
def github_finder():
    if request.method == 'POST':
        username = request.form['username']
        choice = request.form['choice']

        base_url = f"https://api.github.com/users/{username}"
        user_data = requests.get(base_url).json()

        if choice == '1':
            return render_template('github_result.html', user=user_data, choice="account")
        elif choice == '2':
            repos = requests.get(base_url + '/repos', params={"page": 1, "per_page": 100}).json()
            return render_template('github_result.html', repos=repos, user=user_data, choice="repos")
        elif choice == '3':
            followers = requests.get(base_url + '/followers', params={"page": 1, "per_page": 100}).json()
            return render_template('github_result.html', followers=followers, user=user_data, choice="followers")
        elif choice == '4':
            following = requests.get(base_url + '/following', params={"page": 1, "per_page": 100}).json()
            return render_template('github_result.html', following=following, user=user_data, choice="following")

    return render_template('github.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
