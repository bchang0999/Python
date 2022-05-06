from flask import Flask, render_template, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return redirect('/play')
@app.route('/play')
def play():
    return render_template("index.html")	
@app.route('/play/<int:num>')
def box(num):
    return render_template("index_two.html",num=num)

@app.route('/play/<int:num>/<string:color>')
def color(num, color):
    return render_template("index_three.html", num = num, color=color) 

























if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

