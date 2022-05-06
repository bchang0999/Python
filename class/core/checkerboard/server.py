from flask import Flask, render_template, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/4')
def play():
    return render_template("index_two.html")	

@app.route('/<int:x>/<int:y>')
def box(x,y):
    return render_template("index_three.html",x=x, y=y)

















if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.