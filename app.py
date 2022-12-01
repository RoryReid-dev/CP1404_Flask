from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World!</h1>'


@app.route('/greet')
@app.route('/greet/rory')
def greet(name="Rory"):
    return f"Hello {name}"


@app.route('/temperature')
@app.route('/temperature/<celsius>')
def f(celsius=""):
    conversion = convert_celsius_to_fahrenheit(celsius=celsius)
    output = f"<h1>Converting: {celsius}c (celsius) >>> Fahrenheit</h1>\n{celsius}c = {conversion}f"
    return output


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit"""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
