from flask import *
app = Flask(__name__)

@app.route('/')
def hello_world(name=None): 
    return render_template('test.html', name=name)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',)