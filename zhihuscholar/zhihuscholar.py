from flask import Flask, render_template
import sqlite3


app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return render_template('index.html', title='Home')


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


if __name__ == '__main__':
    app.run()
