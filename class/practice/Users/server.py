
from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)
@app.route('/')
def index():
    Users = User.get_all()
    return render_template('index.html', all_users = Users)

@app.route('/create_user')
def create():
    return render_template('create.html')
    

@app.route('/back_at_it_again', methods=["POST"])
def mozaltov():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "hobby" : request.form["hobby"]
    }
    User.save(data)
    return redirect('/')










if __name__=="__main__":
    app.run(debug=True)



