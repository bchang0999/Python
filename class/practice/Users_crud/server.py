from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)
@app.route('/')
def index():
    Users = User.get_all()
    return render_template('home.html', all_users = Users)

@app.route('/create_user')
def create():

    return render_template('create.html')
    


#create
@app.route('/back_at_it_again', methods=["POST"])
def mozaltov():
    data = {
        # "id": request.form["id"],
        "full_name" : request.form["full_name"],
        "Email" : request.form["Email"]
    }
    User.save(data)
    return redirect('/')


#delete
@app.route('/delete/<int:id>')
def bombsaway(id):
    data = {
        "id" : id
    }
    User.delete(data)
    return redirect('/')


#update redirect to page
@app.route('/update/<int:id>')
def update(id):
    return render_template('edit_user.html')

#update function
@app.route('/updated', methods=["POST"])
def changeisagoodthing(data):
    data = {
        "full_name" :request.form["full_name"],
        "email" :request.form["email"]
    }
    User.update(data)
    return redirect('/')















if __name__=="__main__":
    app.run(debug=True)