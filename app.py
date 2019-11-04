from flask import Flask
#from controllers.calculator_controller import calculator

app = Flask(__name__)

@app.route('/')
def hello():
    return 'HELLO WORLD'

if __name__ == "__main__":
    app.run()