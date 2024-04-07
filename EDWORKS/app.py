from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/works')
def works():
    return render_template('works.html')

if __name__ == '__main__':
    app.run()
