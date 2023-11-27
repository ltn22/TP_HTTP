from flask import Flask

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


