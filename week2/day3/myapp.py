
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'ansah britwum kwabena\n am 13 years old\n i love Ghana'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


