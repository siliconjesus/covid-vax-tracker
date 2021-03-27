from flask import Flask, render_template
import configparser

# Get the configuration from the ini file.
config = configparser.ConfigParser()
config.sections
config.read('app.ini')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/md')
def mdvax():
    return render_template('state.html')

if __name__ == '__main__':
    app.run()