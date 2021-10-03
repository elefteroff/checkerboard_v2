from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html', num1 = 4, num2 = 4)

@app.route('/<int:x>')
def checkerboard_row(x):
    return render_template('index.html', num1 = x, num2 = x)

@app.route('/<int:x>/<int:y>')
def cb_row_colomn(x,y):
    return render_template('index.html', num1 = x, num2 = y, color1 = 'red', color2 = 'black')

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def cb_row_colomn_colors(x,y,color1, color2):
    return render_template('index.html', num1 = x, num2 = y, color1 = color1, color2 = color2)
    
if __name__=="__main__":
    app.run(debug=True)
