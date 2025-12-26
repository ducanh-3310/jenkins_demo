from flask import Flask, request, jsonify
from calculator import cal

app = Flask(__name__)

@app.route('/')
def home():
    return "Calculator Web API is running!!!ahihhi"

@app.route('/add')
def add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    calc = cal(a, b)
    return jsonify({"result": calc.add()})

@app.route('/sub')
def sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    calc = cal(a, b)
    return jsonify({"result": calc.sub()})

@app.route('/mul')
def mul():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    calc = cal(a, b)
    return jsonify({"result": calc.mul()})

@app.route('/div')
def div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    calc = cal(a, b)
    return jsonify({"result": calc.div()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
