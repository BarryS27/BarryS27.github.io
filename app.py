from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/work.html')
def work():
    return render_template("work.html")

@app.route('/404.html')
def render_404_static():
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
