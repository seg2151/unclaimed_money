__author__ = 'SGarcia'

from flask import Flask, render_template, request, session, make_response

app = Flask(__name__)
app.secret_key = 'sebbybear'

@app.route('/')
def index_template():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)