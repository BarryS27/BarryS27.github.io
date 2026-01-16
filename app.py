from flask import Flask, render_template
from datetime import datetime, timezone

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.context_processor
def inject_now():
    return {'now': datetime.now(timezone.utc)}

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/work')
def work():
    return render_template("work.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/404.html')
def render_404():
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)