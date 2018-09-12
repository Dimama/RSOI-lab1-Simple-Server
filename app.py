from flask import Flask, render_template, request
from functions import is_palindrome, possible_palindrome
import os

app = Flask(__name__)


@app.route('/possible', methods=['GET'])
def possible_palindrome_route():
    
    word = request.args.get('word')
    if word is None:
        return render_template('usage.html', error=True)

    res = possible_palindrome(word)
    return render_template('result.html',
        name="Is possible to make palindrome from sequence?", word=word, res=res)

  
@app.route('/ispalindrome', methods=['GET'])
def is_palindrome_route():
    
    word = request.args.get('word')
    if word is None:
        return render_template('usage.html', error=True)

    res = is_palindrome(word)
    return render_template('result.html',
        name="Is sequence a palindrome?", word=word, res=res)


@app.route('/')
def hello_world():
	return render_template('usage.html', error=False)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('usage.html', error=True)


if __name__ == '__main__':	
	app.run(host='0.0.0.0', port=int(os.environ.get('PORT')))
