from flask import *
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('login.html')
@app.route('/login')
def logout():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/dash')
def dash():
    return render_template('dash.html')
@app.route('/user')
def user():
    return render_template('Users.html')
@app.route('/book')
def book():
    return render_template('book.html')
@app.route('/transaction')
def trans():
    return render_template('transaction.html')
@app.route('/issuebook')
def issue():
    return render_template('issued.html')
if __name__=='__main__':
    app.run(debug=True)