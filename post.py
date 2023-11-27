from flask import Flask
from flask import render_template
from flask import request

app = Flask("My First Web Server")

count = 0

@app.route('/')
def hello_world():
    return "Hello World"

@app.route("/counter")
def counter_page():
    global count
    
    count += 1
    return "displayed {} times".format(count)


@app.route("/setup", methods=["GET"])
def setup():
    return  render_template ("post.template", text="counter value")


@app.route("/reset", methods=["POST"])
def reset():
    global count
    
    value = request.form["value"]
    print (type(value))
    try:
        count = int(value)
        return "counter set to {}".format(count)
    except:
        return {"message": "Not an Integer"}, 406
    
