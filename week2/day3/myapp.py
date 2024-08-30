
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'ansah britwum kwabena'


@app.route('/whereami')
def whereami():
    return 'Ghana!'

from flask import Flask, render_template
@app.route('/g')
def indexg():
    return render_template('index.html')


from flask import Flask, render_template

@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)

@app.route("/myname/<name>")
def cool(name):
    print(name)
    return render_template("myname.html")

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')
 

