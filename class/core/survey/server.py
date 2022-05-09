from flask import Flask, render_template, redirect,request, session
app = Flask(__name__)
app.secret_key = "letspasspython"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['post'])
def results():
    session["name"]=request.form["name"]
    session["location"]=request.form["location"]
    session["languages"]=request.form["languages"]
    session["big_tex"]=request.form["big_tex"]
    return render_template('index_two.html')








if __name__=="__main__":
    app.run(debug=True)