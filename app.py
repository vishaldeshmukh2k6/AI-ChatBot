from flask import Flask, render_template, request, session, redirect, url_for
from responses import get_bot_response
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.permanent_session_lifetime = timedelta(days=7)

@app.route('/', methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(debug=True, port="5001")
