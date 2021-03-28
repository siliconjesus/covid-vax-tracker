from flask import Flask, render_template
import configparser

# Get the configuration from the ini file.
config = configparser.ConfigParser()
config.sections
config.read('app.ini')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/state/<state>')
def statevax(state):
    return render_template('state.html', state={state})

if __name__ == '__main__':
    app.run()