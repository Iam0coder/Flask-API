from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

def get_random_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        return response.json()
    else:
        return {"content": "Could not retrieve a quote at this time.", "author": "API"}

@app.route('/')
def home():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)

@app.route('/quote')
def quote():
    quote = get_random_quote()
    return jsonify(quote)

if __name__ == '__main__':
    app.run(debug=True)
