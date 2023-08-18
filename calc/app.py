"""Calculator Flask application."""

from flask import Flask, request
import operations


app = Flask(__name__)


@app.route('/add')
def add_numbers():
    """Add two numbers."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    msg = operations.add(a, b)
    return str(msg)


@app.route('/sub')
def subtract_numbers():
    """Subtract two numbers."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    msg = operations.sub(a, b)
    return str(msg)


@app.route('/mult')
def multiply_numbers():
    """Multiply two numbers."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    msg = operations.mult(a, b)
    return str(msg)

@app.route('/div')
def divide_numbers():
    """Divide two numbers."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    msg = operations.div(a, b)
    return str(msg)

operators = {
        "add": operations.add,
        "sub": operations.sub,
        "mult": operations.mult,
        "div": operations.div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)