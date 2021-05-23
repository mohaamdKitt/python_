from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')

def levle1():
    return render_template('index.html',num_row=8,num_col=8)

@app.route('/4')

def levle2():
    return render_template('index.html',num_row=8, num_col=4)

@app.route('/<num1>/<num2>')

def levle3(num1,num2):
    return render_template('index.html',num_row=int(num1), num_col=int(num2))


@app.route('/<num1>/<num2>/<color1>/<color2>')

def levle4(num1, num2, color1, color2):
    return render_template('index.html',num_row=int(num1), num_col=int(num2),color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)