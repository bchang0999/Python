from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "imgoingtofailpython"

@app.route('/')
def index():
    if 'keynamecanbe_anyname' in session:
        session['keynamecanbe_anyname'] += 1
    else:
        session['keynamecanbe_anyname'] = 1
    return render_template('index.html')

@app.route('/STOP_HAMMERTIME', methods= ['post'])
def destroy():
    session.clear()
    return redirect('/')

@app.route('/upwasasadmovie', methods = ['post'])
def count():
    session['keynamecanbe_anyname'] += 1
    return redirect('/')






if __name__=="__main__":
    app.run(debug=True)

