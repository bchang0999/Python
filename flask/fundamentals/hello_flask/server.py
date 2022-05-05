from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'dojo'

@app.route('/say/<name>')
def name(name):
    return name

@app.route('/repeat/<num>/<word>')
def zebra(num,word):
    return word * int(num)

@app.route('/<name>')
def name(name):
    return "Sorry! No Response.Try again."



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

