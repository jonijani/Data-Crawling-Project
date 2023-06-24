from flask import Flask

app = Flask(__name__)  # __name__ accepts file name 

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/hi')
def hi():
    return 'hello junaid it hi function'

@app.route('/joni')
def junaid():
    return 'Helloooo junaid'

if __name__ == '__main__':
    app.run()




