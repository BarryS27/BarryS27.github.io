from flask_frozen import Freezer
from app import app

app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    print("Success!")
