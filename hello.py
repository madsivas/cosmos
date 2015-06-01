from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return '<h2><i>Hello Mad World!</i></h2>'

if __name__ == '__main__':
  app.run(debug=True)
