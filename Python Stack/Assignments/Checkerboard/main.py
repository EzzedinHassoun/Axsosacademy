from flask import Flask,render_template

app=Flask(__name__)

@app.route ("/")

def x_yz():
    
    return render_template ('index.html',x=8,y=8,color1="black",color2="red")

@app.route ("/<int:x>")

def x_y(x):
    return render_template ('index.html',x=x,y=8,color1="black",color2="red")

@app.route("/<int:x>/<int:y>")

def custom_board(x,y):
    return render_template ('index.html',x=x,y=y,color1="black",color2="red")
    
@app.route("/<int:x>/<int:y>/<color1>/<color2>")

def alternating_colors(x,y,color1,color2):
    return render_template('index.html',x=x,y=y,color1=color1,color2=color2)
if __name__=="__main__":
    app.run(debug=True,port=5000)