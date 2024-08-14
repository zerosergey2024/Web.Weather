from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    quote = get_random_quote()
    return render_template('task.html', quote=quote)

def get_random_quote():
    url = "http://api.forismatic.com/api/1.0//random"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"content": "Не удалось получить цитату.", "author": "Неизвестный"}

if __name__ == '__main__':
    app.run(debug=True)