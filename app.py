from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/work.html')
def work():
    return render_template("work.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
