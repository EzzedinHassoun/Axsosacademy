from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/Champion")
def Champion():
    return "Champion!"

@app.route("/say/Flask")
def Hi(name):
    return "Hi Flask!"

@app.route("/say/Michael")
def go(name):
    return "Hi Michael!"

@app.route("/say/John")
def up(name):
    return "Hi John!"

@app.route ("/repeat/<int:num>/<word>")
def word(num , word):
    temp_str = ""
    for i in range(num):
        temp_str += f"{word} "
    return temp_str
    
if __name__=="__main__":
    app.run(debug=True,port=9000)